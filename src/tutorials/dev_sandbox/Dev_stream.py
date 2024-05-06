"""
tests on stream
"""
from string import lower


def contains_c_in(words):
    print(list(filter(lambda x: "c" in x, map(lambda x: lower(x), words))))


def odd_numbers_from(numbers):
    print(filter(lambda x: x % 2, numbers))


def sorted_of(numbers):
    print("normal: {}\nsorted: {}".format(numbers, sorted(numbers)))


def product_of_all(numbers):
    print(reduce((lambda x, y: x * y), numbers))


if __name__ == "__main__":
    integers = [2, 13, 1, 2, 3, 5, 2, 8, 2]
    languages = ['Python', 'Ruby', 'Java', 'C++', 'Ruby', 'C']
    contains_c_in(languages)
    odd_numbers_from(integers)
    sorted_of(integers)
    product_of_all(integers)
