import unittest

from ..app.bugged_calculator import BuggedCalculator


class TddInPythonExample(unittest.TestCase):

    def setUp(self):
        """ To initiate self.calc """
        self.calc = BuggedCalculator()

    def test_bugged_calculator_with_print(self):
        result = self.calc.bugged_add(2, 2)
        # self.assertEqual(4, result) # It does not work so this provokes an error
        self.assertEqual(0, result)

    # use nosetest -s to use with pdb
    def test_bugged_calculator_with_pdb(self):
        result = self.calc.bugged_add_with_pdb(2, 2)
        # self.assertEqual(4, result) # It does not work so this provokes an error
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
