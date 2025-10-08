#!/usr/bin/env python3
"""
Test runner for tumblr_crawler_requests.py unit tests
"""

import unittest
import sys
import os

# Add the parent directory to Python path to import the crawler
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the test module
from test_tumblr_crawler_requests import TestEnhancedTumblrCrawler

def run_tests():
    """Run all unit tests"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestEnhancedTumblrCrawler)
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code based on test results
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    exit_code = run_tests()
    sys.exit(exit_code)
