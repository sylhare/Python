#!/usr/bin/env python3
"""
Example script showing how to use the Tumblr crawler programmatically
"""

from tumblr_crawler import TumblrCrawler


def main():
    """Example usage of the Tumblr crawler"""
    
    # Example 1: Crawl a public blog
    print("Example 1: Crawling a public blog")
    crawler = TumblrCrawler("https://example-blog.tumblr.com")
    try:
        crawler.crawl_blog()
        print("Public blog crawling completed!")
    except Exception as e:
        print(f"Error crawling public blog: {e}")
    
    # Example 2: Crawl with Tumblr account login
    print("\nExample 2: Crawling with Tumblr account login")
    account_crawler = TumblrCrawler(
        "https://example-blog.tumblr.com",
        username="your-email@example.com",
        account_password="your-tumblr-password"
    )
    try:
        account_crawler.crawl_blog()
        print("Account-based crawling completed!")
    except Exception as e:
        print(f"Error crawling with account: {e}")
    
    # Example 3: Crawl a private blog with password
    print("\nExample 3: Crawling a private blog")
    private_crawler = TumblrCrawler(
        "https://private-blog.tumblr.com", 
        password="blog-password-here"
    )
    try:
        private_crawler.crawl_blog()
        print("Private blog crawling completed!")
    except Exception as e:
        print(f"Error crawling private blog: {e}")
    
    # Example 4: Crawl with both account login and private blog password
    print("\nExample 4: Crawling with both account login and private blog password")
    full_auth_crawler = TumblrCrawler(
        "https://private-blog.tumblr.com",
        password="blog-password-here",
        username="your-email@example.com",
        account_password="your-tumblr-password"
    )
    try:
        full_auth_crawler.crawl_blog()
        print("Full authentication crawling completed!")
    except Exception as e:
        print(f"Error crawling with full authentication: {e}")


if __name__ == "__main__":
    main()
