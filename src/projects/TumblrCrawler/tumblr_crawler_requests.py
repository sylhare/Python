#!/usr/bin/env python3
"""
Enhanced Tumblr crawler that handles modern Tumblr blogs with dynamic content
"""

import sys
import os
import re
import json
import time
import subprocess
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class EnhancedTumblrCrawler:
    """Enhanced crawler for modern Tumblr blogs"""
    
    def __init__(self, blog_url: str, username: str = None, password: str = None):
        self.blog_url = blog_url.rstrip('/')
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        })
        
        # Extract blog name from URL for folder naming
        self.blog_name = self._extract_blog_name(blog_url)
        
        # Authenticate if credentials provided
        if username and password:
            self._authenticate()
        
        # Create output directories with blog name
        self.output_dir = Path(f"extracted_{self.blog_name}")
        self.img_dir = self.output_dir / "img"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.img_dir.mkdir(parents=True, exist_ok=True)
        
        self.processed_posts = set()
        self.daily_counters = {}
    
    def _extract_blog_name(self, blog_url):
        """Extract blog name from URL for folder naming"""
        try:
            from urllib.parse import urlparse
            
            # Parse the URL
            parsed = urlparse(blog_url)
            
            # Handle different URL formats
            if 'tumblr.com' in parsed.netloc:
                # For tumblr.com URLs like https://www.tumblr.com/example-blog
                path_parts = parsed.path.strip('/').split('/')
                if path_parts and path_parts[0]:
                    blog_name = path_parts[0]
                else:
                    # Fallback to domain name
                    blog_name = parsed.netloc.replace('www.', '').replace('.tumblr.com', '')
            else:
                # For other domains, use the domain name
                blog_name = parsed.netloc.replace('www.', '')
            
            # Clean up the blog name for filesystem use
            import re
            blog_name = re.sub(r'[^\w\-_.]', '_', blog_name)
            blog_name = blog_name.strip('_')
            
            # Ensure it's not empty
            if not blog_name:
                blog_name = "unknown_blog"
            
            print(f"📁 Blog name extracted: {blog_name}")
            return blog_name
            
        except Exception as e:
            print(f"⚠️  Error extracting blog name: {e}")
            return "unknown_blog"
    
    def _authenticate(self):
        """Authenticate with Tumblr"""
        try:
            print("Authenticating with Tumblr...")
            
            # Get login page
            login_url = "https://www.tumblr.com/login"
            response = self.session.get(login_url)
            
            if response.status_code != 200:
                print("Failed to access login page")
                return False
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find login form
            form = soup.find('form', {'action': '/login'}) or soup.find('form', {'method': 'post'})
            if not form:
                print("Could not find login form")
                return False
            
            # Extract form data
            form_data = {}
            for input_tag in form.find_all('input'):
                name = input_tag.get('name')
                value = input_tag.get('value', '')
                if name:
                    form_data[name] = value
            
            # Add credentials
            form_data['user[email]'] = self.username
            form_data['user[password]'] = self.password
            
            # Submit login form
            action_url = urljoin(login_url, form.get('action', '/login'))
            response = self.session.post(action_url, data=form_data, allow_redirects=True)
            
            # Check if login was successful
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                if any(indicator in response.text.lower() for indicator in 
                      ['dashboard', 'logout', 'settings', 'new post', 'following']):
                    print("✓ Successfully logged into Tumblr")
                    return True
            
            print("Login failed - check credentials")
            return False
            
        except Exception as e:
            print(f"Authentication error: {e}")
            return False
    
    def crawl_blog(self):
        """Main crawling method"""
        print(f"Starting enhanced crawl of: {self.blog_url}")
        
        # First, let's debug what we can see on the page
        self._debug_page_content()
        
        # Try to get posts using direct navigation
        posts = self._get_posts_via_api()
        
        if not posts:
            print("No posts found via direct navigation, trying alternative methods...")
            posts = self._get_posts_alternative()
        
        print(f"Found {len(posts)} posts to process")
        
        # Process each post
        for i, post in enumerate(posts):
            try:
                print(f"Processing post {i+1}/{len(posts)}: {post.get('title', post.get('id', 'Unknown'))}")
                self._process_post(post)
            except Exception as e:
                print(f"Error processing post: {e}")
                continue
        
        print(f"Crawling completed! Content saved to {self.output_dir}")
        
        # Verify image downloads
        self._verify_image_downloads()
    
    def _debug_page_content(self):
        """Debug method to see what's on the page"""
        try:
            print("🔍 Debugging page content...")
            response = self.session.get(self.blog_url)
            print(f"Status code: {response.status_code}")
            print(f"Content length: {len(response.content)}")
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Check for various elements
            print("\n📊 Page analysis:")
            print(f"  - Title: {soup.title.string if soup.title else 'No title'}")
            print(f"  - Meta description: {soup.find('meta', {'name': 'description'})}")
            
            # Check for different post containers
            selectors_to_check = [
                'article',
                '[data-post-id]',
                '.post',
                '.tumblr-post',
                'div[class*="post"]',
                'div[class*="entry"]'
            ]
            
            for selector in selectors_to_check:
                elements = soup.select(selector)
                print(f"  - {selector}: {len(elements)} elements")
                if elements and len(elements) <= 5:  # Show details for small numbers
                    for i, elem in enumerate(elements[:3]):
                        classes = elem.get('class', [])
                        data_attrs = {k: v for k, v in elem.attrs.items() if k.startswith('data-')}
                        print(f"    [{i+1}] Classes: {classes}, Data: {data_attrs}")
            
            # Check for script tags with potential data
            scripts = soup.find_all('script')
            print(f"  - Script tags: {len(scripts)}")
            
            for script in scripts:
                if script.string and ('post' in script.string.lower() or 'tumblr' in script.string.lower()):
                    print(f"    - Script with potential data: {len(script.string)} chars")
                    # Show first 200 chars
                    preview = script.string[:200].replace('\n', ' ').replace('\r', ' ')
                    print(f"      Preview: {preview}...")
            
            print()
            
        except Exception as e:
            print(f"Debug error: {e}")
    
    def _get_posts_via_api(self):
        """Try to get posts by navigating the blog directly"""
        try:
            print("Navigating blog directly...")
            
            # First, try to get the main blog page
            response = self.session.get(self.blog_url)
            if response.status_code != 200:
                print(f"Failed to access blog: {response.status_code}")
                return []
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Try blog-specific extraction first
            print("Trying blog-specific extraction...")
            posts = self._extract_posts_from_blog_structure(soup)
            if posts:
                print(f"Found {len(posts)} posts using blog-specific selectors")
            else:
                # Fallback to general extraction
                posts = self._extract_posts_from_page(soup)
                if posts:
                    print(f"Found {len(posts)} posts on main page using general extraction")
                else:
                    posts = []
            
            # Try pagination to get more posts
            all_posts = posts.copy()
            page = 2
            consecutive_empty_pages = 0
            
            while page <= 20:  # Increased limit to 20 pages
                paginated_urls = [
                    f"{self.blog_url}/page/{page}",
                    f"{self.blog_url}?page={page}",
                    f"{self.blog_url}/archive?page={page}",
                    f"{self.blog_url}?offset={page * 20}"
                ]
                
                page_posts = []
                successful_url = None
                
                for url in paginated_urls:
                    try:
                        print(f"Trying page {page}: {url}")
                        response = self.session.get(url)
                        if response.status_code == 200:
                            soup = BeautifulSoup(response.content, 'html.parser')
                            page_posts = self._extract_posts_from_page(soup)
                            
                            # Also try blog-specific extraction
                            if not page_posts:
                                page_posts = self._extract_posts_from_blog_structure(soup)
                            
                            if page_posts:
                                print(f"Found {len(page_posts)} posts on page {page} using {url}")
                                successful_url = url
                                break
                    except Exception as e:
                        print(f"Error loading page {page} with {url}: {e}")
                        continue
                
                if not page_posts:
                    consecutive_empty_pages += 1
                    print(f"No posts found on page {page}")
                    if consecutive_empty_pages >= 3:  # Stop after 3 consecutive empty pages
                        print(f"No more posts found after page {page-1}")
                        break
                else:
                    consecutive_empty_pages = 0  # Reset counter
                    
                    # Filter out duplicate posts by ID
                    existing_ids = {post.get('id') for post in all_posts}
                    new_posts = [post for post in page_posts if post.get('id') not in existing_ids]
                    
                    if new_posts:
                        all_posts.extend(new_posts)
                        print(f"Added {len(new_posts)} new posts (filtered {len(page_posts) - len(new_posts)} duplicates)")
                        print(f"Total posts so far: {len(all_posts)}")
                    else:
                        print(f"All {len(page_posts)} posts on page {page} were duplicates - stopping pagination")
                        break
                
                page += 1
                
                # Add delay to be respectful
                time.sleep(1)
            
            return all_posts
            
        except Exception as e:
            print(f"Error in navigation method: {e}")
            return []
    
    def _extract_posts_from_page(self, soup):
        """Extract posts from the actual blog page HTML"""
        posts = []
        
        # Look for different post containers that Tumblr might use
        post_selectors = [
            'article[data-post-id]',
            'article.post',
            '.post',
            '.tumblr-post',
            '[data-post-id]',
            'article',
            '.post-wrapper',
            '.entry'
        ]
        
        for selector in post_selectors:
            elements = soup.select(selector)
            if elements:
                print(f"Found {len(elements)} posts using selector: {selector}")
                for element in elements:
                    post = self._extract_post_from_element(element)
                    if post:
                        posts.append(post)
                break
        
        # Also look for JSON data in script tags
        json_posts = self._extract_posts_from_json(soup)
        if json_posts:
            print(f"Found {len(json_posts)} posts from JSON data")
            posts.extend(json_posts)
        
        return posts
    
    def _extract_posts_from_blog_structure(self, soup):
        """Extract posts specifically from blog structure"""
        posts = []
        
        # Look for the specific post structure used by this blog
        # This blog uses: div.post.text, div.post.photoset, div.post.photo
        post_elements = soup.find_all('div', class_=lambda x: x and any(
            cls in ['post', 'text', 'photoset', 'photo'] for cls in (x if isinstance(x, list) else [x])
        ))
        
        print(f"Found {len(post_elements)} potential post elements")
        
        for element in post_elements:
            # Check if it's actually a post (has date and content)
            date_elem = element.find('div', class_='date')
            content_elem = element.find('div', class_='content')
            
            if date_elem and content_elem:
                post = self._extract_post_from_element(element)
                if post:
                    posts.append(post)
                    print(f"✅ Extracted post: {post.get('title', 'No title')[:50]}...")
        
        return posts
    
    def _extract_post_from_element(self, element):
        """Extract post data from a single post element"""
        try:
            post = {}
            
            # Get post ID - try multiple methods
            post_id = element.get('data-post-id') or element.get('id', '')
            
            # If no data-post-id, try to extract from links
            if not post_id:
                links = element.find_all('a', href=True)
                for link in links:
                    href = link['href']
                    # Look for post ID in URL patterns like /post/123456 or /image/123456
                    import re
                    match = re.search(r'/(?:post|image)/(\d+)', href)
                    if match:
                        post_id = match.group(1)
                        break
            
            # If still no post ID, generate one from content hash
            if not post_id:
                content_hash = hash(element.get_text().strip())
                post_id = f"post_{abs(content_hash)}"
            
            post['id'] = post_id
            
            # Get post URL
            link = element.find('a', href=True)
            if link:
                post['url'] = urljoin(self.blog_url, link['href'])
            else:
                post['url'] = f"{self.blog_url}/post/{post_id}"
            
            # Get title - try multiple methods including blog structure
            title_elem = element.find(['h1', 'h2', 'h3', '.title', '.post-title', 'h4', '.link'])
            if title_elem:
                # For this blog structure, the title is in h2.link > a
                if title_elem.name == 'h2' and title_elem.get('class') == ['link']:
                    link_elem = title_elem.find('a')
                    if link_elem:
                        post['title'] = link_elem.get_text().strip()
                    else:
                        post['title'] = title_elem.get_text().strip()
                else:
                    post['title'] = title_elem.get_text().strip()
            else:
                # Try to extract title from the first line of text content
                text_content = element.get_text().strip()
                first_line = text_content.split('\n')[0].strip()
                if first_line and len(first_line) < 100:  # Reasonable title length
                    post['title'] = first_line
                else:
                    post['title'] = f"Post {post_id}"
            
            # Get content/body - enhanced for blog structure
            content_elem = element.find(['.post-content', '.entry-content', '.post-body'])
            if content_elem:
                post['body'] = str(content_elem)
            else:
                # For this blog structure, look for content in the .content div
                content_div = element.find('div', class_='content')
                if content_div:
                    # Focus on <p> tags for content extraction
                    paragraphs = content_div.find_all('p')
                    if paragraphs:
                        # Extract text from each paragraph, filtering out date-like content
                        content_parts = []
                        for p in paragraphs:
                            text = p.get_text().strip()
                            # Skip lines that look like dates (e.g., "23 8 / 2013")
                            if text and not re.match(r'^\d{1,2}\s+\d{1,2}\s*/\s*\d{4}$', text):
                                content_parts.append(text)
                        
                        if content_parts:
                            post['body'] = '\n\n'.join(content_parts)
                        else:
                            # Fallback to full content div
                            post['body'] = str(content_div)
                    else:
                        # Fallback to full content div
                        post['body'] = str(content_div)
                else:
                    # If no .content div, try to extract from the main post element
                    # Look for any text content that's not a date
                    all_text = element.get_text().strip()
                    lines = all_text.split('\n')
                    content_lines = []
                    for line in lines:
                        line = line.strip()
                        # Skip lines that look like dates (e.g., "23 8 / 2013")
                        if line and not re.match(r'^\d{1,2}\s+\d{1,2}\s*/\s*\d{4}$', line):
                            content_lines.append(line)
                    
                    if content_lines:
                        post['body'] = '\n\n'.join(content_lines)
                    else:
                        # Final fallback to full element HTML
                        post['body'] = str(element)
            
            # Get date - try multiple selectors including the specific structure
            date_elem = element.find(['time', '.date', '.post-date', '.timestamp', '.published'])
            if date_elem:
                # Handle the specific structure: <div class="date"><p><span class="day">27</span> 10 / 2014</p></div>
                day_span = date_elem.find('span', class_='day')
                if day_span:
                    day = day_span.get_text().strip()
                    # Get the rest of the date text (month/year)
                    date_text = date_elem.get_text().strip()
                    # Remove the day from the text to get month/year
                    month_year = date_text.replace(day, '').strip()
                    # Format as "DD MM YYYY" for better parsing
                    formatted_date = f"{day} {month_year}"
                    post['date'] = formatted_date
                    print(f"📅 Extracted date: '{formatted_date}' from structure with day span")
                else:
                    post['date'] = date_elem.get_text().strip()
                    print(f"📅 Extracted date: '{post['date']}' from standard date element")
            else:
                # Try to find date in the content - look for patterns like "08 6 / 2015"
                content_text = element.get_text()
                import re
                # Look for date patterns like "08 6 / 2015" or "27 10 / 2014"
                date_pattern = r'(\d{1,2})\s+(\d{1,2})\s*/\s*(\d{4})'
                match = re.search(date_pattern, content_text)
                if match:
                    day, month, year = match.groups()
                    formatted_date = f"{day} {month} / {year}"
                    post['date'] = formatted_date
                    print(f"📅 Extracted date from content: '{formatted_date}'")
                else:
                    post['date'] = ''
                    print(f"📅 No date found for post {post_id}")
            
            # Get post type
            post_type = element.get('data-post-type', 'text')
            post['type'] = post_type
            
            # Get images - comprehensive extraction
            images = []
            
            # Method 1: Standard img tags
            for img in element.find_all('img'):
                src = img.get('src') or img.get('data-src') or img.get('data-original') or img.get('data-lazy-src')
                if src:
                    full_url = urljoin(self.blog_url, src)
                    images.append(full_url)
                    print(f"🖼️ Found image (img tag): {full_url}")
            
            # Method 2: Background images in style attributes
            for elem in element.find_all(style=True):
                style = elem['style']
                import re
                # Look for background-image: url(...) patterns
                bg_match = re.search(r'background-image:\s*url\(["\']?([^"\']+)["\']?\)', style)
                if bg_match:
                    bg_url = bg_match.group(1)
                    full_url = urljoin(self.blog_url, bg_url)
                    images.append(full_url)
                    print(f"🖼️ Found image (background): {full_url}")
            
            # Method 3: Data attributes that might contain image URLs
            for elem in element.find_all(attrs={'data-src': True}):
                src = elem.get('data-src')
                if src and not src.startswith('data:'):  # Skip data URIs
                    full_url = urljoin(self.blog_url, src)
                    images.append(full_url)
                    print(f"🖼️ Found image (data-src): {full_url}")
            
            # Method 4: Look for Tumblr-specific image containers
            for img_container in element.find_all(['div', 'figure'], class_=lambda x: x and any(
                keyword in x.lower() for keyword in ['photo', 'image', 'media', 'attachment']
            )):
                # Look for img tags within these containers
                for img in img_container.find_all('img'):
                    src = img.get('src') or img.get('data-src') or img.get('data-original')
                    if src:
                        full_url = urljoin(self.blog_url, src)
                        images.append(full_url)
                        print(f"🖼️ Found image (container): {full_url}")
            
            # Method 5: Look for links that might be images (common in Tumblr)
            for link in element.find_all('a', href=True):
                href = link['href']
                # Check if the link points to an image file
                if any(href.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.gifv']):
                    full_url = urljoin(self.blog_url, href)
                    images.append(full_url)
                    print(f"🖼️ Found image (link): {full_url}")
            
            # Remove duplicates while preserving order
            seen = set()
            unique_images = []
            for img in images:
                if img not in seen:
                    seen.add(img)
                    unique_images.append(img)
            
            post['photos'] = unique_images
            print(f"📸 Total images found for post {post_id}: {len(unique_images)}")
            
            # Get tags
            tags = []
            for tag_elem in element.find_all(['.tag', '.tags a', '[data-tag]']):
                tag_text = tag_elem.get_text().strip()
                if tag_text:
                    tags.append(tag_text)
            post['tags'] = tags
            
            return post
            
        except Exception as e:
            print(f"Error extracting post from element: {e}")
            return None
    
    def _extract_posts_from_json(self, soup):
        """Extract posts from JSON data in script tags"""
        posts = []
        
        for script in soup.find_all('script'):
            if not script.string:
                continue
            
            text = script.string
            
            # Look for various JSON patterns
            json_patterns = [
                r'window\._tumblrPostData\s*=\s*(\{.*?\});',
                r'window\.tumblrPostData\s*=\s*(\{.*?\});',
                r'var\s+postData\s*=\s*(\{.*?\});',
                r'"posts"\s*:\s*(\[.*?\])',
                r'posts:\s*(\[.*?\])',
            ]
            
            for pattern in json_patterns:
                matches = re.findall(pattern, text, re.DOTALL)
                for match in matches:
                    try:
                        data = json.loads(match)
                        if isinstance(data, dict) and 'posts' in data:
                            posts.extend(self._extract_posts_from_api_data(data))
                        elif isinstance(data, list):
                            posts.extend(self._extract_posts_from_api_data({'posts': data}))
                    except json.JSONDecodeError:
                        continue
        
        return posts
    
    def _extract_posts_from_api_data(self, data):
        """Extract posts from modern API response"""
        posts = []
        
        # Handle different API response formats
        if 'response' in data and 'posts' in data['response']:
            posts_data = data['response']['posts']
        elif 'posts' in data:
            posts_data = data['posts']
        else:
            posts_data = data if isinstance(data, list) else []
        
        for post_data in posts_data:
            post = {
                'id': post_data.get('id'),
                'slug': post_data.get('slug', ''),
                'date': post_data.get('date'),
                'title': post_data.get('title', ''),
                'body': post_data.get('body', ''),
                'type': post_data.get('type', ''),
                'url': post_data.get('post_url', ''),
                'tags': post_data.get('tags', []),
                'photos': post_data.get('photos', []),
                'video': post_data.get('video', {}),
                'audio': post_data.get('audio', {}),
                'link': post_data.get('link_url', ''),
                'quote': post_data.get('quote', ''),
                'quote_source': post_data.get('quote_source', ''),
            }
            posts.append(post)
        
        return posts
    
    def _extract_posts_from_legacy_api(self, data):
        """Extract posts from legacy JSONP API response"""
        posts = []
        
        if 'posts' in data:
            for post_data in data['posts']:
                post = {
                    'id': post_data.get('id'),
                    'slug': post_data.get('slug', ''),
                    'date': post_data.get('date'),
                    'title': post_data.get('title', ''),
                    'body': post_data.get('body', ''),
                    'type': post_data.get('type', ''),
                    'url': post_data.get('url', ''),
                    'tags': post_data.get('tags', []),
                    'photos': post_data.get('photos', []),
                }
                posts.append(post)
        
        return posts
    
    def _get_posts_alternative(self):
        """Alternative method to get posts by scraping the page"""
        try:
            response = self.session.get(self.blog_url)
            if response.status_code != 200:
                return []
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for JSON data in script tags
            posts = []
            for script in soup.find_all('script'):
                if script.string and ('posts' in script.string or 'tumblr' in script.string):
                    try:
                        # Try to extract JSON data
                        text = script.string
                        json_matches = re.findall(r'\{[^{}]*"posts"[^{}]*\}', text)
                        for match in json_matches:
                            try:
                                data = json.loads(match)
                                if 'posts' in data:
                                    posts.extend(self._extract_posts_from_api_data(data))
                            except:
                                continue
                    except:
                        continue
            
            return posts
            
        except Exception as e:
            print(f"Error in alternative method: {e}")
            return []
    
    def _process_post(self, post):
        """Process a single post and save it"""
        post_id = post.get('id', 'unknown')
        if post_id in self.processed_posts:
            return
        
        self.processed_posts.add(post_id)
        
        # Generate filename
        date = self._parse_date(post.get('date', ''))
        if not date:
            date = datetime.now()
        
        date_str = date.strftime("%Y-%m-%d")
        counter = self.daily_counters.get(date_str, 0) + 1
        self.daily_counters[date_str] = counter
        
        title = post.get('title', post.get('slug', 'untitled'))
        filename = self._generate_filename(date_str, title, counter)
        
        # Create markdown content
        content = self._create_markdown_content(post, post_id)
        
        # Save file
        file_path = self.output_dir / filename
        print(f"Attempting to save to: {file_path.absolute()}")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Saved: {filename}")
    
    def _is_date_title(self, title):
        """Check if title is just a date in DD MM / YYYY format"""
        return bool(re.match(r'^\d{1,2}\s+\d{1,2}\s*/\s*\d{4}$', title.strip()))
    
    def _format_title(self, title, date_str):
        """Format title properly - convert date titles to 'Jour DD / MM / YYYY' format"""
        if self._is_date_title(title):
            # Extract date from the title and format it properly
            match = re.match(r'^(\d{1,2})\s+(\d{1,2})\s*/\s*(\d{4})$', title.strip())
            if match:
                day, month, year = match.groups()
                return f"Jour {int(day)} / {int(month)} / {year}"
        
        # For non-date titles, clean them up (replace spaces with hyphens)
        return re.sub(r'\s+', '-', title.strip())
    
    def _generate_filename(self, date_str, title, counter):
        """Generate a clean filename"""
        # Check if title is just a date
        if self._is_date_title(title):
            # Use "article" for date-only titles
            safe_title = "article"
        else:
            # Clean the title for filename use
            safe_title = re.sub(r'[^\w\s-]', '', title).strip()
            safe_title = re.sub(r'\s+', '-', safe_title)[:50]
            if not safe_title:
                safe_title = "untitled"
        
        return f"{date_str}-{safe_title}-{counter}.md"
    
    def _create_markdown_content(self, post, post_id):
        """Create markdown content from post data"""
        lines = []
        
        # Title - format properly
        title = post.get('title', post.get('slug', 'Untitled'))
        if title:
            formatted_title = self._format_title(title, post.get('date', ''))
            lines.append(f"# {formatted_title}")
            lines.append("")
        
        # No metadata separator - clean content only
        
        # Content based on post type
        post_type = post.get('type', 'text')
        
        # Handle images and videos - download and reference locally
        if post.get('photos'):
            print(f"📸 Processing {len(post['photos'])} images for post {post_id}")
            for i, photo_url in enumerate(post['photos']):
                if isinstance(photo_url, str):
                    # Download media and get local path
                    local_path = self._download_media(photo_url, post.get('id', 'unknown'), i)
                    # Check file type and use appropriate markdown
                    if local_path.endswith('.gif') and not local_path.startswith('http'):
                        # GIF files - use image tag
                        lines.append(f"![GIF]({local_path})")
                    elif local_path.endswith(('.mp4', '.webm', '.avi', '.mov')) and not local_path.startswith('http'):
                        # Video files - use video tag
                        lines.append(f"<video controls><source src=\"{local_path}\" type=\"video/mp4\">Your browser does not support the video tag.</video>")
                    elif local_path.endswith(('.gifv',)) or (local_path.startswith('http') and '.gifv' in local_path):
                        # For .gifv URLs that couldn't be downloaded, use a link
                        lines.append(f"[Video]({local_path})")
                    else:
                        # Regular images
                        lines.append(f"![Image]({local_path})")
                    lines.append("")
                elif isinstance(photo_url, dict) and 'original_size' in photo_url:
                    img_url = photo_url['original_size']['url']
                    local_path = self._download_media(img_url, post.get('id', 'unknown'), i)
                    # Check file type and use appropriate markdown
                    if local_path.endswith('.gif') and not local_path.startswith('http'):
                        # GIF files - use image tag
                        lines.append(f"![GIF]({local_path})")
                    elif local_path.endswith(('.mp4', '.webm', '.avi', '.mov')) and not local_path.startswith('http'):
                        # Video files - use video tag
                        lines.append(f"<video controls><source src=\"{local_path}\" type=\"video/mp4\">Your browser does not support the video tag.</video>")
                    elif local_path.endswith(('.gifv',)) or (local_path.startswith('http') and '.gifv' in local_path):
                        # For .gifv URLs that couldn't be downloaded, use a link
                        lines.append(f"[Video]({local_path})")
                    else:
                        # Regular images
                        lines.append(f"![Image]({local_path})")
                    lines.append("")
        
        elif post_type == 'video' and post.get('video'):
            video_url = post['video'].get('video_url', '')
            if video_url:
                lines.append(f"[Video]({video_url})")
                lines.append("")
        
        elif post_type == 'audio' and post.get('audio'):
            audio_url = post['audio'].get('audio_url', '')
            if audio_url:
                lines.append(f"[Audio]({audio_url})")
                lines.append("")
        
        elif post_type == 'link' and post.get('link'):
            lines.append(f"[Link]({post['link']})")
            lines.append("")
        
        elif post_type == 'quote' and post.get('quote'):
            lines.append(f"> {post['quote']}")
            if post.get('quote_source'):
                lines.append(f"*— {post['quote_source']}*")
            lines.append("")
        
        # Body content
        if post.get('body'):
            body = post['body']
            
            # If body is HTML, convert to markdown
            if '<' in body and '>' in body:
                # Convert HTML to markdown (basic conversion)
                body = re.sub(r'<br\s*/?>', '\n', body)
                body = re.sub(r'<p[^>]*>', '\n', body)
                body = re.sub(r'</p>', '\n', body)
                body = re.sub(r'<div[^>]*>', '\n', body)
                body = re.sub(r'</div>', '\n', body)
                body = re.sub(r'<[^>]+>', '', body)  # Remove remaining HTML tags
            else:
                # Body is already text, just clean it up
                body = body.strip()
            
            # Clean up extra whitespace
            body = re.sub(r'\n\s*\n', '\n\n', body)  # Replace multiple newlines with double newline
            body = body.strip()
            
            if body:
                lines.append(body)
        
        return '\n'.join(lines)
    
    def _parse_date(self, date_str):
        """Parse date string"""
        if not date_str:
            return None
        
        try:
            # Clean up the date string
            date_str = date_str.strip()
            print(f"🔍 Parsing date: '{date_str}'")
            
            # Try different date formats including the new format
            formats = [
                '%Y-%m-%d %H:%M:%S GMT',
                '%Y-%m-%d %H:%M:%S',
                '%Y-%m-%d',
                '%d %b %Y',
                '%B %d, %Y',
                '%d %m / %Y',  # For "27 10 / 2014" format (day month year)
                '%d %m/%Y',    # For "27 10/2014" format (day month year)
                '%d %m %Y',    # For "27 10 2014" format (day month year)
            ]
            
            for fmt in formats:
                try:
                    result = datetime.strptime(date_str, fmt)
                    print(f"✅ Successfully parsed date: {result} using format: {fmt}")
                    return result
                except ValueError:
                    continue
            
            # Handle special case: "27 10 / 2014" -> "27 10 2014"
            if ' / ' in date_str:
                cleaned_date = date_str.replace(' / ', ' ')
                try:
                    result = datetime.strptime(cleaned_date, '%d %m %Y')
                    print(f"✅ Successfully parsed date: {result} after cleaning spaces")
                    return result
                except ValueError:
                    pass
            
            # Try parsing with dateutil if available
            try:
                from dateutil import parser
                result = parser.parse(date_str)
                print(f"✅ Successfully parsed date with dateutil: {result}")
                return result
            except ImportError:
                pass
            
        except Exception:
            pass
        
        return None
    
    def _download_media(self, url, post_id, media_index):
        """Download an image or video and return the local filename"""
        try:
            # Get file extension
            parsed_url = urlparse(url)
            path = parsed_url.path
            ext = os.path.splitext(path)[1]
            
            # Handle .gifv files - convert to .mp4 for better compatibility
            if ext == '.gifv':
                ext = '.mp4'
                print(f"Converting .gifv to .mp4: {url}")
            
            if not ext:
                ext = '.jpg'  # Default extension

            # Create filename
            filename = f"{post_id}_{media_index}{ext}"
            file_path = self.img_dir / filename

            # Skip if already downloaded
            if file_path.exists():
                return str(file_path.relative_to(self.output_dir))

            # Download with proper headers
            print(f"Downloading media: {url}")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'image/webp,image/apng,image/*,video/mp4,video/webm,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Referer': self.blog_url,
            }
            
            response = self.session.get(url, stream=True, headers=headers, timeout=30)
            response.raise_for_status()
            
            # Check content type - accept both images and videos
            content_type = response.headers.get('content-type', '').lower()
            is_media = any(media_type in content_type for media_type in [
                'image/', 'video/', 'application/octet-stream'
            ])
            
            if not is_media:
                print(f"Warning: {url} returned content-type {content_type}, not media")
                return url  # Return original URL if not media

            # Save file
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            # Verify the file was saved correctly by checking its size
            if file_path.stat().st_size == 0:
                print(f"Warning: Downloaded file {filename} is empty")
                file_path.unlink()  # Delete empty file
                return url

            print(f"Saved media: {filename} ({file_path.stat().st_size} bytes)")
            
            # If it's a video file, try to convert to GIF
            if ext in ['.mp4', '.webm', '.avi', '.mov']:
                gif_filename = f"{post_id}_{media_index}.gif"
                gif_path = self.img_dir / gif_filename
                
                if self._convert_to_gif(file_path, gif_path):
                    # Return the GIF path instead of the video path
                    return str(gif_path.relative_to(self.output_dir))
                else:
                    # If conversion failed, return the original video path
                    print(f"GIF conversion failed, using original video: {filename}")
            
            return str(file_path.relative_to(self.output_dir))

        except Exception as e:
            print(f"Error downloading media {url}: {e}")
            return url  # Return original URL if download fails
    
    def _convert_to_gif(self, video_path, gif_path, max_width=500, max_duration=10):
        """Convert video file to GIF using FFmpeg"""
        try:
            # Check if FFmpeg is available
            try:
                subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                print("FFmpeg not found, skipping GIF conversion")
                return False
            
            # Check if input file exists
            if not Path(video_path).exists():
                print(f"Video file not found: {video_path}")
                return False
            
            # Check if GIF already exists
            if Path(gif_path).exists():
                print(f"GIF already exists: {gif_path}")
                return True
            
            print(f"Converting {video_path} to GIF...")
            
            # FFmpeg command to convert video to GIF
            cmd = [
                'ffmpeg',
                '-i', str(video_path),
                '-vf', f'scale={max_width}:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse',
                '-t', str(max_duration),  # Limit duration to avoid huge files
                '-loop', '0',  # Loop the GIF
                '-y',  # Overwrite output file
                str(gif_path)
            ]
            
            # Run FFmpeg command
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"Successfully converted to GIF: {gif_path}")
                return True
            else:
                print(f"FFmpeg error: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"Error converting to GIF: {e}")
            return False
    
    def _verify_image_downloads(self):
        """Verify that all images were successfully downloaded"""
        try:
            if not self.img_dir.exists():
                print("📁 No images directory found - no images were downloaded")
                return
            
            # Count downloaded files
            image_files = list(self.img_dir.glob('*'))
            total_images = len(image_files)
            
            if total_images == 0:
                print("⚠️ No images were downloaded")
                return
            
            # Count by file type
            file_types = {}
            for img_file in image_files:
                ext = img_file.suffix.lower()
                file_types[ext] = file_types.get(ext, 0) + 1
            
            print(f"\n📸 Image Download Summary:")
            print(f"   Total images downloaded: {total_images}")
            print(f"   Images directory: {self.img_dir}")
            
            for ext, count in sorted(file_types.items()):
                print(f"   {ext or 'no extension'}: {count} files")
            
            # Check for any empty files
            empty_files = [f for f in image_files if f.stat().st_size == 0]
            if empty_files:
                print(f"⚠️ Warning: {len(empty_files)} empty files found:")
                for f in empty_files[:5]:  # Show first 5
                    print(f"   - {f.name}")
                if len(empty_files) > 5:
                    print(f"   ... and {len(empty_files) - 5} more")
            
            print(f"✅ Image verification completed")
            
        except Exception as e:
            print(f"Error verifying image downloads: {e}")

def main():
    """Main function to test the enhanced crawler"""
    blog_url = "https://example-blog.tumblr.com/"
    
    print("Enhanced Tumblr Crawler")
    print("=" * 30)
    
    crawler = EnhancedTumblrCrawler(blog_url)
    crawler.crawl_blog()

if __name__ == "__main__":
    main()
