"""
To work with nosetests:
  pip install nose
  sudo eqsy_install nose

Creating a Test file:
First, we import the standard unittest module from the Python standard library.
Next, we need a class to contain the different test cases.
Finally, a method is required for the test itself, with the only requirement being that it is named with "test_"
at the beginning, so that it may be picked up and executed by the nosetest runner
"""

import unittest
from app.calculator import Calculator


class TddInPythonExample(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)

    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')

    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)

    def test_calculator_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')


# You can execute the test using the standard unittest runner, or do
# nosetests test_calculator.py
if __name__ == '__main__':
    unittest.main()