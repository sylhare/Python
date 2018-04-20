import unittest

class AbstractTestCase(unittest.TestCase):

    def test_generic_input_one(self):
        result = self.function("input 1")
        self.assertTrue(result)

    def test_generic_input_two(self):
        result = self.function("input 2")
        self.assertTrue(result)