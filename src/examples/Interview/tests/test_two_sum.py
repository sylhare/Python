"""
Two Sum

Given an array of integers and a target number.
It returns true if the array possesses two different numbers which added gives the number.

Let's assume that if there's a solution, there's only one.
You can't sum two times the multiple element

"""
import datetime
import re
import unittest

from ..questions.two_sum import *


def verify_two_sum(your_algorithm):
    class TwoSumTestCase(unittest.TestCase):

        def setUp(self):
            self.start_time = datetime.datetime.now()

        def test_example_1(self):
            self.assertTrue(your_algorithm([4, 1, 2, 4], 8))

        def test_example_2(self):
            self.assertFalse(your_algorithm([1, 2, 3, 4], 8))

        def test_example_3(self):
            self.assertTrue(your_algorithm([2, 7, 11, 15], 9))

        def test_example_4(self):
            self.assertTrue(your_algorithm([4, 4, 1, 2], 8))

        def tearDown(self):
            name = re.search(r'Test.*$', self.id()).group(0)
            elapse = (datetime.datetime.now() - self.start_time).microseconds
            print("{} - Time: {}ms".format(name, elapse))

    return TwoSumTestCase


class TestA(verify_two_sum(brute_force_check)):
    pass


class TestB(verify_two_sum(functional_brute_force_check)):
    pass


class TestC(verify_two_sum(variable_check)):
    pass
