import unittest
import datetime
from ..tests import *
from ..converter.converter import *


class TestConverter(unittest.TestCase):

    def test_csv_transpose(self):
        """ Make sure that transpose can transpose the csv and put it back how it was """
        self.assertEqual(TEST_DATA_ROW, transpose(TEST_DATA_COLUMN))
        self.assertEqual(TEST_DATA_COLUMN, transpose(TEST_DATA_ROW))

    def test_string_to_date(self):
        """ If it is really converted the first character should not be a # """
        self.assertTrue(string_to_date("18/04/2018") == datetime.date(2018, 4, 18))

    def test_string_to_float(self):
        """ If it is really converted the first character should not be a # """
        self.assertTrue(string_to_float("1234.5678") == 1234.5678)


if __name__ == "__main__":
    unittest.main()
