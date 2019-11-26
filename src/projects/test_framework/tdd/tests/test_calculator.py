"""
To work with nosetests:
  pip install nose
  sudo eqsy_install nose

# https://automationpanda.com/2017/03/14/python-testing-101-pytest/
To work with pytest:
  pip install pytest
  python -m pytest
  python -m pytest --junitxml= # Generate JUnit-style XML test reports

    With coverage
      pip install pytest-cov
      python -m pytest --cov=app --cov-report=term


Creating a Test file:
First, we import the standard unittest module from the Python standard library.
Next, we need a class to contain the different test cases.
Finally, a method is required for the test itself, with the only requirement being that it is named with "test_"
at the beginning, so that it may be picked up and executed by the nosetest runner
"""

import unittest

from ..app.calculator import Calculator


class TddInPythonExample(unittest.TestCase):

    def setUp(self):
        """ To be executed before the tests"""

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

    def test_subtract(self):
        value = self.calc.subtract(3, 2)
        assert value == 1.0

    def test_subtract_negative(self):
        value = self.calc.subtract(2, 3)
        assert value == -1.0

    def test_multiply(self):
        value = self.calc.multiply(3, 2)
        assert value == 6.0

    def test_divide(self):
        value = self.calc.divide(3, 2)
        assert value == 1.5


# You can execute the test using the standard unittest runner, or do
# nosetests test_calculator.py
if __name__ == '__main__':
    unittest.main()
