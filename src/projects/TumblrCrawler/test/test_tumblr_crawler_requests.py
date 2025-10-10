#!/usr/bin/env python3
"""
Unit tests for tumblr_crawler_requests.py
"""

import unittest
import tempfile
import shutil
import json
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime
from bs4 import BeautifulSoup

# Import the crawler class
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tumblr_crawler_requests import EnhancedTumblrCrawler


class TestEnhancedTumblrCrawler(unittest.TestCase):
    """Test cases for EnhancedTumblrCrawler"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_blog_url = "https://test-blog.tumblr.com"
        
        # Create crawler instance with temporary directory
        with patch.object(Path, 'mkdir'):
            self.crawler = EnhancedTumblrCrawler(self.test_blog_url)
            self.crawler.output_dir = Path(self.temp_dir)
            self.crawler.img_dir = self.crawler.output_dir / "img"
    
    def tearDown(self):
        """Clean up after each test method."""
        shutil.rmtree(self.temp_dir)
    
    def test_init(self):
        """Test crawler initialization"""
        self.assertEqual(self.crawler.blog_url, self.test_blog_url)
        self.assertIsNone(self.crawler.username)
        self.assertIsNone(self.crawler.password)
        self.assertIsInstance(self.crawler.processed_posts, set)
        self.assertIsInstance(self.crawler.daily_counters, dict)
    
    def test_init_with_credentials(self):
        """Test crawler initialization with credentials"""
        with patch.object(EnhancedTumblrCrawler, '_authenticate') as mock_auth:
            crawler = EnhancedTumblrCrawler(
                self.test_blog_url, 
                username="test_user", 
                password="test_pass"
            )
            self.assertEqual(crawler.username, "test_user")
            self.assertEqual(crawler.password, "test_pass")
            mock_auth.assert_called_once()
    
    def test_parse_date_valid_formats(self):
        """Test date parsing with valid date formats"""
        test_cases = [
            ("2023-12-25 10:30:00 GMT", datetime(2023, 12, 25, 10, 30, 0)),
            ("2023-12-25 10:30:00", datetime(2023, 12, 25, 10, 30, 0)),
            ("2023-12-25", datetime(2023, 12, 25)),
            ("25 Dec 2023", datetime(2023, 12, 25)),
            ("December 25, 2023", datetime(2023, 12, 25)),
        ]
        
        for date_str, expected in test_cases:
            with self.subTest(date_str=date_str):
                result = self.crawler._parse_date(date_str)
                self.assertEqual(result, expected)
    
    def test_parse_date_invalid_formats(self):
        """Test date parsing with invalid date formats"""
        invalid_dates = [
            "",
            None,
            "invalid date",
            "not a date at all",
            "2023-13-45",  # Invalid month/day
        ]
        
        for date_str in invalid_dates:
            with self.subTest(date_str=date_str):
                result = self.crawler._parse_date(date_str)
                self.assertIsNone(result)
    
    def test_extract_post_from_element_with_data_post_id(self):
        """Test post extraction from element with data-post-id"""
        # Create mock element with data-post-id
        element_html = '''
        <div class="post" data-post-id="123456">
            <h2 class="title">Test Post Title</h2>
            <div class="content">Test post content</div>
            <a href="/post/123456">Read more</a>
            <img src="https://example.com/image.jpg" alt="Test image">
        </div>
        '''
        soup = BeautifulSoup(element_html, 'html.parser')
        element = soup.find('div', class_='post')
        
        result = self.crawler._extract_post_from_element(element)
        
        self.assertIsNotNone(result)
        self.assertEqual(result['id'], '123456')
        self.assertEqual(result['title'], 'Test Post Title')
        self.assertEqual(result['url'], f"{self.test_blog_url}/post/123456")
        self.assertIn('https://example.com/image.jpg', result['photos'])
    
    def test_extract_post_from_element_without_data_post_id(self):
        """Test post extraction from element without data-post-id"""
        # Create mock element without data-post-id but with post link
        element_html = '''
        <div class="post">
            <h2 class="title">Test Post Title</h2>
            <div class="content">Test post content</div>
            <a href="/post/789012">Read more</a>
        </div>
        '''
        soup = BeautifulSoup(element_html, 'html.parser')
        element = soup.find('div', class_='post')
        
        result = self.crawler._extract_post_from_element(element)
        
        self.assertIsNotNone(result)
        self.assertEqual(result['id'], '789012')  # Extracted from link
        self.assertEqual(result['title'], 'Test Post Title')
        self.assertEqual(result['url'], f"{self.test_blog_url}/post/789012")
    
    def test_extract_post_from_element_no_id(self):
        """Test post extraction from element with no ID"""
        # Create mock element with no ID or post links
        element_html = '''
        <div class="post">
            <h2 class="title">Test Post Title</h2>
            <div class="content">Test post content</div>
        </div>
        '''
        soup = BeautifulSoup(element_html, 'html.parser')
        element = soup.find('div', class_='post')
        
        result = self.crawler._extract_post_from_element(element)
        
        self.assertIsNotNone(result)
        self.assertTrue(result['id'].startswith('post_'))  # Generated ID
        self.assertEqual(result['title'], 'Test Post Title')
    
    def test_create_markdown_content(self):
        """Test markdown content creation"""
        post_data = {
            'id': '123456',
            'title': 'Test Post',
            'date': '2023-12-25',
            'type': 'text',
            'url': 'https://test-blog.tumblr.com/post/123456',
            'tags': ['test', 'example'],
            'body': '<p>This is test content</p>',
            'photos': ['https://example.com/image.jpg']
        }
        
        with patch.object(self.crawler, '_download_media', return_value='img/test.jpg'):
            result = self.crawler._create_markdown_content(post_data, '123456')
        
        self.assertIn('# Test-Post', result)
        self.assertIn('![Image](img/test.jpg)', result)
        self.assertIn('This is test content', result)
    
    def test_create_markdown_content_without_images(self):
        """Test markdown content creation without images"""
        post_data = {
            'id': '123456',
            'title': 'Test Post',
            'date': '2023-12-25',
            'type': 'text',
            'url': 'https://test-blog.tumblr.com/post/123456',
            'tags': [],
            'body': 'Simple text content',
            'photos': []
        }
        
        result = self.crawler._create_markdown_content(post_data, '123456')
        
        self.assertIn('# Test-Post', result)
        self.assertIn('Simple text content', result)
        self.assertNotIn('![Image]', result)
    
    def test_download_media_success(self):
        """Test successful image download"""
        test_url = "https://example.com/test-image.jpg"
        post_id = "123456"
        image_index = 0
        
        # Ensure the img directory exists
        self.crawler.img_dir.mkdir(parents=True, exist_ok=True)
        
        # Mock the requests session
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {'content-type': 'image/jpeg'}
        mock_response.iter_content.return_value = [b'fake image data']
        
        with patch.object(self.crawler.session, 'get', return_value=mock_response):
            result = self.crawler._download_media(test_url, post_id, image_index)
        
        self.assertEqual(result, f"img/{post_id}_{image_index}.jpg")
        
        # Check if file was created
        expected_file = self.crawler.img_dir / f"{post_id}_{image_index}.jpg"
        self.assertTrue(expected_file.exists())
    
    def test_download_media_failure(self):
        """Test image download failure"""
        test_url = "https://example.com/nonexistent.jpg"
        post_id = "123456"
        image_index = 0
        
        # Mock the requests session to raise an exception
        with patch.object(self.crawler.session, 'get', side_effect=Exception("Network error")):
            result = self.crawler._download_media(test_url, post_id, image_index)
        
        # Should return original URL on failure
        self.assertEqual(result, test_url)
    
    def test_download_media_already_exists(self):
        """Test image download when file already exists"""
        test_url = "https://example.com/test-image.jpg"
        post_id = "123456"
        image_index = 0
        
        # Create the file first
        expected_file = self.crawler.img_dir / f"{post_id}_{image_index}.jpg"
        expected_file.parent.mkdir(parents=True, exist_ok=True)
        expected_file.write_text("existing content")
        
        # Mock the requests session
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {'content-type': 'image/jpeg'}
        mock_response.iter_content.return_value = [b'new image data']
        
        with patch.object(self.crawler.session, 'get', return_value=mock_response):
            result = self.crawler._download_media(test_url, post_id, image_index)
        
        # Should return existing file path without downloading
        self.assertEqual(result, f"img/{post_id}_{image_index}.jpg")
        
        # Content should not be overwritten
        self.assertEqual(expected_file.read_text(), "existing content")
    
    def test_extract_posts_from_json(self):
        """Test extracting posts from JSON data in script tags"""
        # Create mock soup with JSON data
        json_data = {
            "posts": [
                {
                    "id": "123456",
                    "title": "Test Post",
                    "body": "Test content",
                    "date": "2023-12-25",
                    "type": "text",
                    "url": "https://test-blog.tumblr.com/post/123456"
                }
            ]
        }
        
        script_html = f'<script>window._tumblrPostData = {json.dumps(json_data)};</script>'
        soup = BeautifulSoup(script_html, 'html.parser')
        
        result = self.crawler._extract_posts_from_json(soup)
        
        # The method might find multiple patterns, so check if our expected post is in the results
        self.assertGreaterEqual(len(result), 1)
        # Find our test post in the results
        test_post = next((post for post in result if post.get('id') == '123456'), None)
        self.assertIsNotNone(test_post)
        self.assertEqual(test_post['title'], 'Test Post')
    
    def test_extract_posts_from_json_no_data(self):
        """Test extracting posts from JSON when no data is found"""
        # Create mock soup without JSON data
        script_html = '<script>var someOtherData = "not tumblr data";</script>'
        soup = BeautifulSoup(script_html, 'html.parser')
        
        result = self.crawler._extract_posts_from_json(soup)
        
        self.assertEqual(len(result), 0)
    
    def test_extract_posts_from_page(self):
        """Test extracting posts from a page"""
        # Create mock HTML with posts
        html_content = '''
        <html>
            <body>
                <div class="post" data-post-id="123456">
                    <h2>Post 1</h2>
                    <div class="content">Content 1</div>
                </div>
                <div class="post" data-post-id="789012">
                    <h2>Post 2</h2>
                    <div class="content">Content 2</div>
                </div>
            </body>
        </html>
        '''
        soup = BeautifulSoup(html_content, 'html.parser')
        
        result = self.crawler._extract_posts_from_page(soup)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['id'], '123456')
        self.assertEqual(result[1]['id'], '789012')
    
    @patch('requests.Session.get')
    def test_crawl_blog_mock(self, mock_get):
        """Test the main crawl_blog method with mocked requests"""
        # Mock the response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = '''
        <html>
            <body>
                <div class="post" data-post-id="123456">
                    <h2>Test Post</h2>
                    <div class="content">Test content</div>
                </div>
            </body>
        </html>
        '''
        mock_get.return_value = mock_response
        
        # Mock the file writing and processing
        with patch('builtins.open', mock_open()) as mock_file:
            with patch.object(Path, 'write_text'):
                with patch.object(self.crawler, '_process_post'):
                    self.crawler.crawl_blog()
        
        # Verify that the request was made
        mock_get.assert_called()
    
    def test_process_post_duplicate_prevention(self):
        """Test that duplicate posts are not processed twice"""
        post_data = {
            'id': '123456',
            'title': 'Test Post',
            'date': '2023-12-25',
            'type': 'text',
            'url': 'https://test-blog.tumblr.com/post/123456',
            'tags': [],
            'body': 'Test content',
            'photos': []
        }
        
        # Process the same post twice
        with patch.object(self.crawler, '_create_markdown_content', return_value='# Test'):
            with patch('builtins.open', mock_open()):
                with patch.object(Path, 'write_text'):
                    # First processing
                    self.crawler._process_post(post_data)
                    self.assertIn('123456', self.crawler.processed_posts)
                    
                    # Second processing should be skipped
                    self.crawler._process_post(post_data)
                    # Should still only have one entry
                    self.assertEqual(len(self.crawler.processed_posts), 1)


def mock_open():
    """Helper function to create a mock file object"""
    from unittest.mock import mock_open as original_mock_open
    return original_mock_open()


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)
