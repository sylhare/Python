"""
Main crawler module for extracting Tumblr content
"""

import os
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from tqdm import tqdm


class TumblrCrawler:
    """Main class for crawling Tumblr blogs and extracting content"""
    
    def __init__(self, blog_url: str, password: Optional[str] = None, 
                 username: Optional[str] = None, account_password: Optional[str] = None):
        """
        Initialize the Tumblr crawler
        
        Args:
            blog_url: URL of the Tumblr blog to crawl
            password: Optional password for private blogs
            username: Optional Tumblr username for account login
            account_password: Optional Tumblr password for account login
        """
        self.blog_url = blog_url.rstrip('/')
        self.password = password
        self.username = username
        self.account_password = account_password
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Create output directories
        self.output_dir = Path("extracted")
        self.img_dir = self.output_dir / "img"
        self.img_dir.mkdir(parents=True, exist_ok=True)
        
        # Track processed content to avoid duplicates
        self.processed_posts = set()
        self.daily_counters = {}
        
    def authenticate(self) -> bool:
        """
        Authenticate with Tumblr account and/or private blog if credentials are provided
        
        Returns:
            True if authentication successful or not needed, False otherwise
        """
        # First, try to authenticate with Tumblr account if credentials provided
        if self.username and self.account_password:
            if not self._authenticate_tumblr_account():
                return False
        
        # Then check if blog requires password
        if not self.password:
            return True
            
        # Try to access the blog first
        try:
            response = self.session.get(self.blog_url)
            if response.status_code == 200:
                # Check if it's a private blog
                soup = BeautifulSoup(response.content, 'html.parser')
                if 'password' in soup.get_text().lower():
                    # This is a private blog, attempt authentication
                    return self._authenticate_private_blog()
                return True
        except requests.RequestException:
            pass
            
        return False
    
    def _authenticate_tumblr_account(self) -> bool:
        """
        Authenticate with Tumblr account using username and password
        
        Returns:
            True if authentication successful, False otherwise
        """
        try:
            # Get the login page
            login_url = "https://www.tumblr.com/login"
            response = self.session.get(login_url)
            
            if response.status_code != 200:
                return False
                
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the login form
            form = soup.find('form', {'action': '/login'}) or soup.find('form', {'method': 'post'})
            if not form:
                return False
            
            # Extract form data including CSRF token
            form_data = {}
            for input_tag in form.find_all('input'):
                name = input_tag.get('name')
                value = input_tag.get('value', '')
                if name:
                    form_data[name] = value
            
            # Add login credentials
            form_data['user[email]'] = self.username
            form_data['user[password]'] = self.account_password
            
            # Submit the login form
            action_url = urljoin(login_url, form.get('action', '/login'))
            response = self.session.post(action_url, data=form_data, allow_redirects=True)
            
            # Check if login was successful
            if response.status_code == 200:
                # Look for indicators of successful login
                soup = BeautifulSoup(response.content, 'html.parser')
                # Check for dashboard or user-specific content
                if any(indicator in response.text.lower() for indicator in 
                      ['dashboard', 'logout', 'settings', 'new post', 'following']):
                    print("✓ Successfully logged into Tumblr account")
                    return True
            
            return False
            
        except Exception as e:
            print(f"Error during Tumblr account authentication: {e}")
            return False
    
    def _authenticate_private_blog(self) -> bool:
        """
        Authenticate with a private Tumblr blog
        
        Returns:
            True if authentication successful, False otherwise
        """
        try:
            # Get the password form
            response = self.session.get(self.blog_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the password form
            form = soup.find('form', {'method': 'post'})
            if not form:
                return False
                
            # Extract form data
            form_data = {}
            for input_tag in form.find_all('input'):
                name = input_tag.get('name')
                value = input_tag.get('value', '')
                if name:
                    form_data[name] = value
                    
            # Add password
            form_data['password'] = self.password
            
            # Submit the form
            action_url = urljoin(self.blog_url, form.get('action', ''))
            response = self.session.post(action_url, data=form_data)
            
            return response.status_code == 200 and 'password' not in response.text.lower()
            
        except Exception:
            return False
    
    def crawl_blog(self) -> None:
        """Main method to crawl the entire blog"""
        if not self.authenticate():
            raise Exception("Failed to authenticate with the blog")
            
        print(f"Starting to crawl blog: {self.blog_url}")
        
        # Get all posts
        posts = self._get_all_posts()
        print(f"Found {len(posts)} posts to process")
        
        # Process each post
        for post in tqdm(posts, desc="Processing posts"):
            try:
                self._process_post(post)
            except Exception as e:
                print(f"Error processing post {post.get('url', 'unknown')}: {e}")
                continue
                
        print(f"Crawling completed! Content saved to {self.output_dir}")
    
    def _get_all_posts(self) -> List[Dict]:
        """
        Get all posts from the blog
        
        Returns:
            List of post dictionaries
        """
        posts = []
        page = 0
        
        while True:
            try:
                # Try different pagination patterns
                paginated_urls = [
                    f"{self.blog_url}/page/{page}",
                    f"{self.blog_url}?page={page}",
                    f"{self.blog_url}/archive?page={page}",
                ]
                
                page_posts = []
                for url in paginated_urls:
                    try:
                        response = self.session.get(url)
                        if response.status_code == 200:
                            page_posts = self._extract_posts_from_page(response.content)
                            if page_posts:
                                break
                    except requests.RequestException:
                        continue
                
                if not page_posts:
                    break
                    
                # Filter out already processed posts
                new_posts = [p for p in page_posts if p.get('url') not in self.processed_posts]
                if not new_posts:
                    break
                    
                posts.extend(new_posts)
                page += 1
                
                # Add delay to be respectful
                time.sleep(1)
                
            except Exception as e:
                print(f"Error getting page {page}: {e}")
                break
                
        return posts
    
    def _extract_posts_from_page(self, content: bytes) -> List[Dict]:
        """
        Extract post information from a page
        
        Args:
            content: HTML content of the page
            
        Returns:
            List of post dictionaries
        """
        soup = BeautifulSoup(content, 'html.parser')
        posts = []
        
        # Look for different post containers
        post_selectors = [
            'article.post',
            '.post',
            '.entry',
            '.post-content',
            '[data-post-id]'
        ]
        
        for selector in post_selectors:
            post_elements = soup.select(selector)
            if post_elements:
                for element in post_elements:
                    post_data = self._extract_post_data(element)
                    if post_data:
                        posts.append(post_data)
                break
                
        return posts
    
    def _extract_post_data(self, element) -> Optional[Dict]:
        """
        Extract data from a post element
        
        Args:
            element: BeautifulSoup element representing a post
            
        Returns:
            Dictionary with post data or None
        """
        try:
            # Extract URL
            url = None
            link = element.find('a', href=True)
            if link:
                url = urljoin(self.blog_url, link['href'])
            else:
                # Try to find URL in data attributes
                url = element.get('data-url') or element.get('data-post-url')
                if url:
                    url = urljoin(self.blog_url, url)
            
            if not url:
                return None
                
            # Extract title
            title = None
            title_elem = element.find(['h1', 'h2', 'h3', '.title', '.post-title'])
            if title_elem:
                title = title_elem.get_text().strip()
            
            # Extract content
            content = None
            content_elem = element.find(['.post-content', '.entry-content', '.content', 'p'])
            if content_elem:
                content = str(content_elem)
            
            # Extract date
            date = None
            date_elem = element.find(['time', '.date', '.post-date', '.timestamp'])
            if date_elem:
                date_text = date_elem.get_text().strip()
                # Try to parse various date formats
                date = self._parse_date(date_text)
            
            # Extract images
            images = []
            img_elements = element.find_all('img')
            for img in img_elements:
                src = img.get('src') or img.get('data-src')
                if src:
                    images.append(urljoin(self.blog_url, src))
            
            return {
                'url': url,
                'title': title,
                'content': content,
                'date': date,
                'images': images,
                'element': element
            }
            
        except Exception as e:
            print(f"Error extracting post data: {e}")
            return None
    
    def _parse_date(self, date_text: str) -> Optional[datetime]:
        """
        Parse date from various formats
        
        Args:
            date_text: Date string to parse
            
        Returns:
            Parsed datetime or None
        """
        from dateutil import parser
        
        try:
            return parser.parse(date_text)
        except:
            return None
    
    def _process_post(self, post: Dict) -> None:
        """
        Process a single post and save it
        
        Args:
            post: Post dictionary
        """
        url = post.get('url')
        if not url or url in self.processed_posts:
            return
            
        self.processed_posts.add(url)
        
        # Get full post content
        try:
            response = self.session.get(url)
            if response.status_code != 200:
                return
                
            soup = BeautifulSoup(response.content, 'html.parser')
            full_content = self._extract_full_post_content(soup)
            
            if not full_content:
                full_content = post.get('content', '')
                
        except requests.RequestException:
            full_content = post.get('content', '')
        
        # Process images
        images = post.get('images', [])
        if full_content:
            # Extract images from content
            content_soup = BeautifulSoup(full_content, 'html.parser')
            content_images = [img.get('src') or img.get('data-src') 
                            for img in content_soup.find_all('img')]
            images.extend([urljoin(self.blog_url, img) for img in content_images if img])
        
        # Download images
        downloaded_images = self._download_images(images)
        
        # Convert to markdown
        markdown_content = self._convert_to_markdown(full_content, downloaded_images)
        
        # Save post
        self._save_post(post, markdown_content)
    
    def _extract_full_post_content(self, soup: BeautifulSoup) -> str:
        """
        Extract full post content from the page
        
        Args:
            soup: BeautifulSoup object of the post page
            
        Returns:
            HTML content of the post
        """
        content_selectors = [
            '.post-content',
            '.entry-content',
            '.content',
            'article',
            '.post',
            'main'
        ]
        
        for selector in content_selectors:
            content_elem = soup.select_one(selector)
            if content_elem:
                return str(content_elem)
                
        return ""
    
    def _download_images(self, image_urls: List[str]) -> List[str]:
        """
        Download images and return local paths
        
        Args:
            image_urls: List of image URLs to download
            
        Returns:
            List of local image paths
        """
        local_paths = []
        
        for i, url in enumerate(image_urls):
            try:
                response = self.session.get(url, stream=True)
                if response.status_code == 200:
                    # Generate filename
                    parsed_url = urlparse(url)
                    filename = os.path.basename(parsed_url.path)
                    if not filename or '.' not in filename:
                        filename = f"image_{i}.jpg"
                    
                    # Ensure unique filename
                    counter = 1
                    original_filename = filename
                    while (self.img_dir / filename).exists():
                        name, ext = os.path.splitext(original_filename)
                        filename = f"{name}_{counter}{ext}"
                        counter += 1
                    
                    # Download and save
                    local_path = self.img_dir / filename
                    with open(local_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    
                    local_paths.append(f"img/{filename}")
                    
            except Exception as e:
                print(f"Error downloading image {url}: {e}")
                continue
                
        return local_paths
    
    def _convert_to_markdown(self, html_content: str, local_images: List[str]) -> str:
        """
        Convert HTML content to markdown with local image references
        
        Args:
            html_content: HTML content to convert
            local_images: List of local image paths
            
        Returns:
            Markdown content
        """
        if not html_content:
            return ""
            
        # Convert to markdown
        markdown = md(html_content, heading_style="ATX")
        
        # Replace image URLs with local paths
        for i, local_path in enumerate(local_images):
            # This is a simple replacement - in practice, you might want more sophisticated matching
            markdown = re.sub(r'!\[.*?\]\([^)]+\)', f'![Image {i+1}]({local_path})', markdown, count=1)
        
        return markdown
    
    def _save_post(self, post: Dict, markdown_content: str) -> None:
        """
        Save post as markdown file
        
        Args:
            post: Post dictionary
            markdown_content: Markdown content to save
        """
        # Generate filename
        date = post.get('date') or datetime.now()
        if isinstance(date, str):
            date = self._parse_date(date) or datetime.now()
            
        date_str = date.strftime("%Y-%m-%d")
        
        # Get counter for this date
        counter = self.daily_counters.get(date_str, 0) + 1
        self.daily_counters[date_str] = counter
        
        # Generate filename
        title = post.get('title', 'untitled')
        safe_title = re.sub(r'[^\w\s-]', '', title).strip()[:50]
        filename = f"{date_str}-article-{counter}.md"
        if safe_title:
            filename = f"{date_str}-{safe_title}-{counter}.md"
        
        # Save file
        file_path = self.output_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {post.get('title', 'Untitled')}\n\n")
            f.write(f"**Date:** {date.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**URL:** {post.get('url', '')}\n\n")
            f.write("---\n\n")
            f.write(markdown_content)
        
        print(f"Saved post: {filename}")
