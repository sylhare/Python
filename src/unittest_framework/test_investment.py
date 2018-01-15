#!/usr/bin/env python
# file: TestInvestment.py

"""
__author__= Tom Bryan
__date__= 2003
__source__= http://starship.python.net/crew/tbryan/UnitTestTalk/slide1.html
"""

import unittest

import investment


class TestInvestment(unittest.TestCase):

    def test_simple(self):
        """Basic functionality of total_interest_continuously"""
        interest = investment.total_interest_continuously(1000, .12, 3)
        self.failIf(abs(interest - 433.33) >= .01)

    def test_long_principal(self):
        """Principal of long type in total_interest_continuously"""
        interest = investment.total_interest_continuously(1000L, .12, 3)
        self.failIf(abs(interest - 433.33) >= .01)

    def test_float_principal(self):
        """Principal of floating point type in total_interest_continuously"""
        interest = investment.total_interest_continuously(1000.00, .12, 3)
        self.failIf(abs(interest - 433.33) >= .01)

    def test_long_time(self):
        """Interest overflowing to infinity and beyond in total_interest_continuously"""
        interest = investment.total_interest_continuously(1000.00, .12, 30000)
        self.assertEqual(interest, float('inf'))

    def test_huge_principal(self):
        """Principal of inf test of in total_interest_continuously"""
        interest = investment.total_interest_continuously(1.0e+1000000, .12, 3)
        self.assertEqual(interest, float('nan'))

    def test_negative_interest(self):
        """Negative interest in total_interest_continuously"""
        interest = investment.total_interest_continuously(1000, -.12, 3)
        self.failIf(abs(-302.32 - interest) >= .01)

    def test_negative_principal(self):
        """Negative principal in total_interest_continuously"""
        self.assertRaises(ValueError,
                          investment.total_interest_continuously,
                          -1000, .12, 3)

    def test_negative_time(self):
        """Negative time in total_interest_continuously"""
        self.assertRaises(ValueError,
                          investment.total_interest_continuously,
                          1000, .12, -3)

    def test_zero_principal(self):
        """Zero principal in total_interest_continuously"""
        interest = investment.total_interest_continuously(0, .12, 3)
        self.assertEqual(interest, 0.0)

    def test_zero_interest(self):
        """Zero interest in total_interest_continuously"""
        interest = investment.total_interest_continuously(1000, 0., 3)
        self.assertEqual(interest, 0.0)


def suite():
    """Returns a suite with one instance of TestInvestment for each
    method starting with the word test."""
    return unittest.makeSuite(TestInvestment, 'test')


def suite2():
    """Returns a suite with the specified instances of TestInvestment.
    Each instance tests the method indicated by its constructor."""
    suite = unittest.TestSuite()
    suite.addTest(TestInvestment("test_negative_time"))
    suite2 = unittest.TestSuite()
    suite2.addTest(TestInvestment("test_zero_interest"))
    suite2.addTest(TestInvestment("test_zero_principal"))
    suite.addTest(suite2)
    return suite


if __name__ == '__main__':
    unittest.main()