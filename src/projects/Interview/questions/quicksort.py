import random


def systemsort(array):
    return sorted(sorted(array), key=len)


def quicksort_str(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[random.randint(0, len(array) - 1)]
    pivot_number = int(pivot)
    pivot_len = len(pivot)

    for item in array:
        item_len = len(item)
        if item_len < pivot_len:
            low.append(item)
        elif item_len == pivot_len:
            item_number = int(item)
            if item_number < pivot_number:
                low.append(item)
            elif item_number > pivot_number:
                high.append(item)
            else:
                same.append(item)
        else:
            high.append(item)

    return quicksort_str(low) + same + quicksort_str(high)


def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[random.randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)


def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array


def insertion_timsort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1

        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array


def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


def timsort(array):
    min_run = 32
    n = len(array)

    for i in range(0, n, min_run):
        insertion_timsort(array, i, min((i + min_run - 1), n - 1))

    size = min_run

    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            array[start:start + len(merged_array)] = merged_array

        size *= 2

    return array
