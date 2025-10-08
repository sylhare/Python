# Tumblr Crawler

A Python web crawler that extracts content from Tumblr blogs and converts it to markdown format with organized image storage.


## Installation

This project uses `uv` for dependency management. Make sure you have `uv` installed:

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then install the project:

```bash
# Navigate to the project directory
cd src/projects/TumblrCrawler

# Install dependencies
uv sync

# Install the package in development mode
uv pip install -e .
```


### Programmatic Usage

```python
from tumblr_crawler import TumblrCrawler

# Create crawler instance for public blog
crawler = TumblrCrawler("https://example.tumblr.com")

# Create crawler with account login
crawler = TumblrCrawler(
    "https://example.tumblr.com", 
    username="your-email@example.com",
    account_password="your-password"
)

# Create crawler with both account login and private blog password
crawler = TumblrCrawler(
    "https://private-blog.tumblr.com",
    password="blog-password",
    username="your-email@example.com", 
    account_password="your-password"
)

# Start crawling
crawler.crawl_blog()
```

## Output Structure

The crawler creates the following directory structure:

```
extracted/
├── img/                          # Downloaded images
│   ├── image_1.jpg
│   ├── image_2.png
│   └── ...
├── 2024-01-15-article-1.md      # Blog posts as markdown
├── 2024-01-15-article-2.md
├── 2024-01-16-my-post-title-1.md
└── ...
```

### File Naming Convention

- **Articles**: `YYYY-MM-DD-article-X.md` or `YYYY-MM-DD-title-X.md`
- **Images**: Original filename preserved, with counter if duplicates exist
- **X**: Counter for multiple posts/images on the same day


## License

This project is open source. Please use responsibly and respect website terms of service.

## Disclaimer

This tool is for educational and personal use only. Please respect Tumblr's terms of service and the rights of content creators. Always ensure you have permission to crawl and download content.
