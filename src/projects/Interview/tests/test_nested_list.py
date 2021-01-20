"""
From a list with name and score:
    - give the second lowest score
    - give the name of everyone with that score ordered alphabetically

"""
import datetime
import re
import unittest

from src.projects.Interview.questions.hacker_rank import get_record_info


def verifyNestedList(your_algorithm):
    class NestedListTestCase(unittest.TestCase):

        def setUp(self):
            self.start_time = datetime.datetime.now()

        def test_example_0(self):
            records = []
            self.assertEqual([None, []], your_algorithm(records))

        def test_example_1(self):
            records = [[]]
            self.assertEqual([None, []], your_algorithm(records))

        def test_example_2(self):
            records = [["Unique", 100]]
            self.assertEqual([100.0, ["Unique"]], your_algorithm(records))

        def test_example_3(self):
            records = [["c", 30], ["b", 60], ["a", 60]]
            self.assertEqual([60.0, ["a", "b"]], your_algorithm(records))

        def test_example_4(self):
            records = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]] 
            self.assertEqual([37.21, ["Berry", "Harry"]], your_algorithm(records))

        def test_example_5(self):
            records = None
            self.assertEqual([None, []], your_algorithm(records))

        def tearDown(self):
            name = re.search(r"Test.*$", self.id()).group(0)
            elapse = (datetime.datetime.now() - self.start_time).microseconds
            print("{} - Time: {}ms".format(name, elapse))

    return NestedListTestCase


class TestA(verifyNestedList(get_record_info)):
    pass


if __name__ == "__main__":
    unittest.main()
