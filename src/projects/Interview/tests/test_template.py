import unittest


class TemplateTest(unittest.TestCase):

    def setUp(self):
        """Initialisation des tests."""

    def test_example_0(self):
        excepted = ""
        actual = ""
        self.assertEqual(excepted, actual)

    def test_example_1(self):
        boolean = True
        self.assertTrue(boolean)

    def test_example_2(self):
        boolean = False
        self.assertFalse(boolean)

    def test_example_3(self):
        actual_list = [""]
        expected_element = ""
        self.assertIn(expected_element, actual_list)


if __name__ == "__main__":
    unittest.main()