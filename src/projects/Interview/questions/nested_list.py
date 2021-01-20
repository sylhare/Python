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


def flatten(nested_list):
    flat_list = []

    for e in nested_list:
        if isinstance(e, list):
            flat_e = flatten(e)
            for sub_element in flat_e:
                    flat_list.append(sub_element)
        else:
            flat_list.append(e)

    return flat_list
