"""
Find Duplicate Number

Given an array of integers from 1 to n of size n + 1.
Prove that there is at least one duplicate number exists.
(Pigeon Hole principle: https://en.wikipedia.org/wiki/Pigeonhole_principle)

There's only one number that has duplicates,
Also that number can have more than 1 duplicate.
"""
import datetime
import re
import resource
import unittest

from ..questions.pigeon import *


def verify_pigeon_hole(your_algorithm):
    class PigeonHoleTestCase(unittest.TestCase):

        def setUp(self):
            self.start_time = datetime.datetime.now()
            self.usage = resource.getrusage(resource.RUSAGE_SELF)

        def test_example_1(self):
            self.assertEqual(2, your_algorithm([1, 3, 4, 2, 2]))

        def test_example_2(self):
            self.assertEqual(1, your_algorithm([1, 3, 4, 1, 2]))

        def test_example_3(self):
            self.assertEqual(3, your_algorithm([1, 3, 4, 3, 2, 3, 6]))

        def test_example_4(self):
            self.assertEqual(6, your_algorithm([1, 4, 6, 2, 6, 3, 5]))

        def tearDown(self):
            name = re.search(r'Test.*$', self.id()).group(0)
            elapse = (datetime.datetime.now() - self.start_time).microseconds
            memory = int((self.usage[2] * resource.getpagesize()) / 1000000.0) - 93860
            print("{} - Time: {}ms, Mem: {}mb".format(name, elapse, memory))

    return PigeonHoleTestCase


class TestA(verify_pigeon_hole(sort_check)):
    pass


class TestB(verify_pigeon_hole(variable_check)):
    pass


class TestC(verify_pigeon_hole(floyd_cycle_check)):
    pass


class TestD(verify_pigeon_hole(collection_check)):
    pass


class TestE(verify_pigeon_hole(enumerate_check)):
    pass


class TestF(verify_pigeon_hole(variable_set_check)):
    pass


if __name__ == '__main__':
    unittest.main()
