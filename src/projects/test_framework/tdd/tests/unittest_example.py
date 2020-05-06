#!/usr/bin/env python3
"""
Simple example of using tests
You would normally have your code in another file in another folder
And your test in a folder named "test".

Here an example of what the folder directory would look like:

package
  - math
      - square.py
      - __init__.py
  - test
      - square_test.py
      - __.init__.py
  - __init__.py

The __init__.py makes the folder as a python module.

In TDD (Test Driven Development) you would first write the test,
then you would implement the code to make the test pass.
Finally you would refactor your code to make it smaller, more lisible
and more integrated with the rest.
"""

# Default python library for unit testing
import unittest


def square(number):
    """ :return: the square of the input number """
    return number * number


class SquareTest(unittest.TestCase):
    """
    SquareTest class to test the square function.
    It inherits from the class "unittest.TestCase" which offers
    all the assertion methods that you will use to test your code.

    "self" refers to the object, you need to use it to access those methods.
    If you are not familiar with the syntax, learn more about classes in python.
    """

    def test_square_positive_number(self):
        """
        Make sure your square function handles positive numbers
        """
        self.assertEqual(4, square(2))
        self.assertEqual(9, square(3))
        self.assertEqual(1, square(1))
        self.assertEqual(0, square(0))

    def test_square_negative_number(self):
        """
        Make sure your square function handles negative numbers
        """
        self.assertEqual(1, square(-1))
        self.assertEqual(4, square(-2))

    def test_square_not_a_number(self):
        """
        If your put anything but a number,
        a TypeError Exception will be launch and your program will
        stop working.
        Usually you handle exception by better controlling inputs or
        using try and catch.
        """
        with self.assertRaises(TypeError):
            square("not a number")


if __name__ == "__main__":
    # You can run this file using:   python unittest_example.py
    unittest.main()
