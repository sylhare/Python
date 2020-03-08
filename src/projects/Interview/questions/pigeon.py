"""
Pigeon hole implementation

Find out in test.test_pigeon if it works
"""


def sort_check(numbers):
    """
    Sorts all the numbers in the array,
    So the duplicates are following each other
    """
    numbers.sort()
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            return i


def variable_check(numbers):
    """
    Add all of the numbers seen in a variable (like a list)
    If already in the variable, then it's a duplicate
    """
    seen = []
    for number in numbers:
        if number in seen:
            return number
        else:
            seen.append(number)


def floyd_cycle_check(numbers):
    """
    works because len(array) = n with for any x: array[x] <= n
    hence it can be considered as a linked list with a loop or cycle
    when tortoise and hare meets,
    hare has traveled twice the distance of tortoise
    so half the distance between the start and the meeting point
    should be the beginning of the loop -> the duplicate number.
    """
    tortoise = numbers[0]
    hare = numbers[0]

    while True:
        tortoise = numbers[tortoise]
        hare = numbers[numbers[hare]]

        if tortoise == hare:
            break  # Meeting point

    from_start = numbers[0]
    from_meeting = tortoise

    while from_start != from_meeting:
        from_start = numbers[from_start]
        from_meeting = numbers[from_meeting]

    return from_meeting
