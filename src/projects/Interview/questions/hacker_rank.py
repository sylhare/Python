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


def create_nested_records():
    print("Enter records length as int, then name as string and grade as number")
    input_length = int(input())
    return [[input(), float(input())] for _ in range(input_length)]


def insert_sort(nested_list):
    for i in range(1, len(nested_list)):
        to_sort = nested_list[i]
        j = i - 1

        while j >= 0 and nested_list[j][1] > to_sort[1]:
            nested_list[j + 1] = nested_list[j]
            j -= 1

        nested_list[j + 1] = to_sort
    return nested_list


def solution_list(nested_list):
    sorted_list = insert_sort(nested_list)
    second_lower = sorted_list[2][1]
    name_with_score = []
    for elem in sorted_list:
        if elem[1] == second_lower:
            name_with_score.append(elem[0])
        if elem[1] > second_lower:
            break
    name_with_score.sort()
    return [float(second_lower), name_with_score]


def get_record_info(nested_list):
    try:
        if len(nested_list) == 1:
            return [float(nested_list[0][1]), [nested_list[0][0]]]
        else:
            return solution_list(nested_list)
    except IndexError:
        print("Input not valid {}".format(nested_list))
    except TypeError:
        print("Input not a nested list {}".format(nested_list))

    return [None, []]
