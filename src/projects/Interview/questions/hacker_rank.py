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


def reverse_sort_insert(result, e):
    """ To insert in the list while keeping it reverse sorted"""
    for count, number in enumerate(result):
        if number < e:
            result.insert(count, e)
            return result

    result.append(e)
    return result


def divide_k_biggest_ones(result, k):
    """ to divide the biggest number even when the biggest has already been divided """
    while k > 0:
        # print("result {} k {}".format(result, k))
        divided = math.ceil(result.pop(0) / 2.0)
        result = reverse_sort_insert(result, divided)
        k = k - 1

    return sum(result)


def minSum(num, k):
    """ gives the minimal sum of a list after k number of divisions """
    result = []
    min_sum = 0
    for e in num:
        result = reverse_sort_insert(result, e)
        # print(result)

        if len(result) > k:
            min_sum += result.pop(len(result) - 1)
            # print("min_sum {} result {}".format(min_sum, result))

    return min_sum + divide_k_biggest_ones(result, k)
