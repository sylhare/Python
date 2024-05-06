"""
From a list with name and score:
    - give the second lowest score
    - give the name of everyone with that score ordered alphabetically

"""
import datetime
import re
import unittest

from src.examples.Interview.questions.nested_list import get_record_info, flatten


class NestedListTestCase(unittest.TestCase):

    def setUp(self):
        self.start_time = datetime.datetime.now()

    def test_example_0(self):
        records = []
        self.assertEqual([None, []], get_record_info(records))

    def test_example_1(self):
        records = [[]]
        self.assertEqual([None, []], get_record_info(records))

    def test_example_2(self):
        records = [["Unique", 100]]
        self.assertEqual([100.0, ["Unique"]], get_record_info(records))

    def test_example_3(self):
        records = [["c", 30], ["b", 60], ["a", 60]]
        self.assertEqual([60.0, ["a", "b"]], get_record_info(records))

    def test_example_4(self):
        records = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]
        self.assertEqual([37.21, ["Berry", "Harry"]], get_record_info(records))

    def test_example_5(self):
        records = None
        self.assertEqual([None, []], get_record_info(records))

    def tearDown(self):
        name = re.search(r"Test.*$", self.id()).group(0)
        elapse = (datetime.datetime.now() - self.start_time).microseconds
        print("{} - Time: {}ms".format(name, elapse))


class FlattenNestedList(unittest.TestCase):

    def test_types(self):
        self.assertTrue(isinstance([], list))
        self.assertTrue(isinstance([0], list))
        self.assertFalse(isinstance({0}, list))
        self.assertFalse(isinstance(tuple([0, 0]), list))

    def test_example_0(self):
        input_list = []
        expected = []
        self.assertEqual(expected, flatten(input_list))

    def test_example_1(self):
        input_list = [[1, 1], 2, [1, 1]]
        expected = [1, 1, 2, 1, 1]
        self.assertEqual(expected, flatten(input_list))

    def test_example_2(self):
        input_list = [1, [4, [6]]]
        expected = [1, 4, 6]
        self.assertEqual(expected, flatten(input_list))

    def test_example_3(self):
        input_list = [2, [4, [6, [8, [10]]]], 12]
        expected = [2, 4, 6, 8, 10, 12]
        self.assertEqual(expected, flatten(input_list))


if __name__ == "__main__":
    unittest.main()
