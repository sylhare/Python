def toggle_boolean(x):
    """
    boolean operation
    """
    return not x


def toggle_xor(x):
    """
    using `^=` operator
    :param x: boolean or 0/1

    x = True
    x ^= True
    -> False

    x = 1
    x ^= 1
    -> 0
    """

    x ^= x

    return x


def toggle_xor_value(x):
    """
    Take one value or the other between `^`
    """
    A = 3
    B = 5
    t = A ^ B

    x ^= t

    return x


def toggle_substraction_value(x):
    """
    With x = 5 or 3
    the toggle values are A and B
    """
    A = 3
    B = 5
    total = A + B

    return total - x


def toggle_dictionary(x):
    """
    with x equal to either A or B
    value and key are crossed
    """

    A = '123'
    B = 'xyz'
    d = {A: B, B: A}

    return d[x]


def toggle_itertool():
    """
    Using itertool with a defined list value
    """
    import itertools

    value = ['red', 'green', 'blue']

    return itertools.cycle(value).__next__()


# python 2
# toggle = itertools.cycle(['red', 'green', 'blue']).next
# python 3
# toggle = itertools.cycle(['red', 'green', 'blue']).__next__
# toggle()

import math
import sys

d = {1: 0, 0: 1}
l = [1, 0]


def exception_approach(x):
    """

    :param x: 
    :return: 
    """
    try:
        return x / x - x / x
    except  ZeroDivisionError:
        return 1


def cosinus_approach(x):
    """

    :param x: 
    :return: 
    """
    return abs(int(math.cos(x * 0.5 * math.pi)))


def module_approach(x):
    """

    :param x: 
    :return: 
    """
    return (x + 1) % 2


def subs_approach(x):
    """

    :param x: 
    :return: 
    """
    return x - 1


def if_approach(x):
    """

    :param x: 
    :return: 
    """
    return 0 if x == 1 else 1


def list_approach(x):
    """

    :param x: 
    :return: 
    """
    global l
    return l[x]


def dict_approach(x):
    """

    :param x: 
    :return: 
    """
    global d
    return d[x]


def xor_approach(x):
    """

    :param x: 
    :return: 
    """
    return x ^ 1


def not_approach(x):
    """

    :param x: 
    :return: 
    """
    b = bool(x)
    p = not b
    return int(p)


funcs = [exception_approach, cosinus_approach, dict_approach, module_approach, subs_approach, if_approach,
         list_approach, xor_approach, not_approach]

f = funcs[int(sys.argv[1])]
print("\n\n\n", f.func_name)
x = 0
for _ in range(0, 100000000):
    x = f(x)

if __name__ == "__main__":
    pass
