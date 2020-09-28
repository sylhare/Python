"""
For hacker rank solutions
"""
import math


def is_leap(year):
    """
    Tells if a year is leap or not
    """
    leap = False

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True

    return leap


VOWELS = ["A", "E", "I", "O", "U", "Y"]


def minion_game_formatter(vowel, consonant):
    """
    Format minion_game answer
    """
    if vowel > consonant:
        result = "Vowel {}".format(vowel)
    else:
        result = "Consonant {}".format(consonant)
    return result


def minion_game(word):
    """
    Tells which vowel or consonant has the most substrings
    """
    vowel = 0
    consonant = 0
    counter = len(word)

    for letter in word:
        if letter in VOWELS:
            vowel += counter
        else:
            consonant += counter
        counter = counter - 1

    return minion_game_formatter(vowel, consonant)


def mid_angle(ab, bc):
    """
    Returns the MBC angle
    """
    return round(math.degrees(math.atan(float(ab) / bc)))
