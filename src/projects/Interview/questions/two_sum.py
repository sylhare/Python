def brute_force_check(array, target):
    """
    Brute force looking with a double loop in all combinations until one works
    Time complexity : O(n^2). For each element, we try to find its complement by looping through the rest of
    array which takes O(n) time. Therefore, the time complexity is O(n^2).
    Space complexity : O(1)
    """
    for i in range(0, len(array) - 1):
        for second in array:
            if array[i] + second == target:
                return True
    return False


def functional_brute_force_check(array, target):
    """
    One liner
    """
    return len(filter(lambda x: x, [target - array[i] in array[i + 1:] for i in range(0, len(array) - 1)])) > 0


def variable_check(array, target):
    """
    Go through each elements once and check if the other remaining element of the division has been seen or not:
    Target = element + x so the seen variables stores all of the possible integer from he array for this equation.
    So if a x is in seen then it means that it's a solution, so we return True.
    Time complexity : O(n). We traverse the list containing n elements only once. Each look up in the table costs only O(1) time.
    Space complexity : O(n). The extra space required depends on the number of items stored in the hash table, which stores at most n elements.

    """
    seen = []
    for value in array:
        if (target - value) in seen:
            return True
        seen.append(value)
    return False
