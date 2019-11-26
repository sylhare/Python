import unittest

from ..app.raise_app import *


def lambda_raise_param():
    return lambda x: raise_if_None(x), None


class TestRaise(unittest.TestCase):

    def test_direct_raise_1(self):
        self.assertRaises(TypeError, raise_directly)

    @unittest.expectedFailure
    def test_direct_raise_1_2(self):
        self.assertRaises(TypeError, raise_directly())

    def test_direct_raise_2(self):
        with self.assertRaises(TypeError):
            raise_directly()

    @unittest.expectedFailure
    def test_direct_raise_3(self):
        self.assertRaises(KeyError, raise_directly)

    def test_raise_with_param_1(self):
        self.assertRaises(ValueError, raise_if_None(None))

    @unittest.expectedFailure
    def test_raise_with_param_1_2(self):
        self.assertRaises(ValueError, raise_if_None, None)

    @unittest.expectedFailure
    def test_raise_with_param_2_1(self):
        with self.assertRaises(ValueError):
            lambda_raise_param()

    @unittest.expectedFailure
    def test_raise_with_param_2_2(self):
        with self.assertRaises(ValueError):
            raise_if_None(None)

    def test_direct_raise_catched(self):
        self.assertRaises(TypeError, raise_directly)

    def test_raise_with_param_catched(self):
        self.assertRaises(ValueError, raise_if_None(None))


if __name__ == '__main__':
    unittest.main()
