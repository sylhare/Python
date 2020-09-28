"""
For Hacker rank examples
"""
import unittest

from ..questions.hacker_rank import *


class HackerRankTest(unittest.TestCase):

    def leap_year_test(self):
        """
        An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day.
        It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun.
        A leap year contains a leap day.

        In the Gregorian calendar, three conditions are used to identify leap years:

            The year can be evenly divided by 4, is a leap year, unless:
                The year can be evenly divided by 100, it is NOT a leap year, unless:
                    The year is also evenly divisible by 400. Then it is a leap year.

        This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300
        and 2500 are NOT leap years.
        """
        self.assertTrue(is_leap(1732))
        self.assertTrue(is_leap(1796))
        self.assertFalse(is_leap(1800))
        self.assertTrue(is_leap(1804))
        self.assertFalse(is_leap(1990))
        self.assertTrue(is_leap(1996))
        self.assertFalse(is_leap(1998))
        self.assertTrue(is_leap(2000))

    def minion_game_test(self):
        """
        Find out of one string which one gives the most substring starting from either a consonant or vowel.
        There are no shuffling of the substring (it always need to be in the same order of the initial word)
        If a substring is part of the original string it's +1 point:

        BA substring of BANANA -> 1
        NA substring of BANANA -> 2
        A substring of BANANA -> 3

        Input BANANA -> Output Consonant 12
        Consonant made more points and 12 the number of points made. (vowel would only score 9 here)
        """
        self.assertEquals("Consonant 12", minion_game("BANANA"))
        self.assertEquals("Consonant 15", minion_game("CLIMAX"))
        self.assertEquals("Vowel 11", minion_game("IGLOOS"))

    def find_the_angle_MBC_test(self):
        """
        Having a triangle ABC with a 90 degrees angle on B
        If you make a line from B to M the middle of the hypotenuse, knowing AB and BC;
        Give the degree of the newly formed angle CBM

        Input AB, BC -> Ouput rounded angle
        """
        self.assertEquals(45, mid_angle(10, 10))
        self.assertEquals(63, mid_angle(10, 5))
        self.assertEquals(27, mid_angle(5, 10))


if __name__ == "__main__":
    unittest.main()
