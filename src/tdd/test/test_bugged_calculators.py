import unittest
from app.calculator import Calculator


class TddInPythonExample(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_bugged_calculator_with_print(self):
        result = self.calc.bugged_add(2, 2)
        self.assertEqual(4, result)

    # use nosetest -s to use with pdb
    def test_bugged_calculator_with_pdb(self):
        result = self.calc.bugged_add_with_pdb(2, 2)
        self.assertEqual(4, result)


if __name__ == '__main__':
    unittest.main()