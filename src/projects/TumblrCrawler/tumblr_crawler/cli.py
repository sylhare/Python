"""
Command-line interface for the Tumblr crawler
"""

import sys
from pathlib import Path

import click

from .crawler import TumblrCrawler


@click.command()
@click.argument('blog_url', type=str)
@click.option('--password', '-p', type=str, help='Password for private blogs')
@click.option('--username', '-u', type=str, help='Tumblr username/email for account login')
@click.option('--account-password', '-a', type=str, help='Tumblr account password for login')
@click.option('--output-dir', '-o', type=str, default='extracted', 
              help='Output directory for extracted content')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
def main(blog_url: str, password: str, username: str, account_password: str, 
         output_dir: str, verbose: bool):
    """
    Crawl a Tumblr blog and extract content to markdown files.
    
    BLOG_URL: URL of the Tumblr blog to crawl (e.g., https://example.tumblr.com)
    """
    try:
        # Validate URL
        if not blog_url.startswith(('http://', 'https://')):
            blog_url = f"https://{blog_url}"
        
        if not blog_url.endswith('.tumblr.com') and 'tumblr.com' not in blog_url:
            click.echo("Warning: This doesn't appear to be a Tumblr URL", err=True)
        
        # Create crawler
        crawler = TumblrCrawler(blog_url, password, username, account_password)
        
        # Override output directory if specified
        if output_dir != 'extracted':
            crawler.output_dir = Path(output_dir)
            crawler.img_dir = crawler.output_dir / "img"
            crawler.img_dir.mkdir(parents=True, exist_ok=True)
        
        if verbose:
            click.echo(f"Blog URL: {blog_url}")
            click.echo(f"Output directory: {crawler.output_dir}")
            if password:
                click.echo("Password provided for private blog")
            if username:
                click.echo(f"Tumblr account login: {username}")
        
        # Start crawling
        click.echo(f"Starting to crawl {blog_url}...")
        crawler.crawl_blog()
        
        click.echo("Crawling completed successfully!")
        
    except KeyboardInterrupt:
        click.echo("\nCrawling interrupted by user", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
