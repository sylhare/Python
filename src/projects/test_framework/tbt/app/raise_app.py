"""
test for raise
"""


def raise_directly():
    raise TypeError


def raise_if_None(param):
    if None:
        raise ValueError
    return param


def raise_directly_but_catched():
    try:
        raise_directly()
    except TypeError as e:
        print("{} has been catched".format(e))


def raise_if_None_but_catched(param):
    try:
        raise_if_None(param)
    except ValueError as e:
        print("{} catched for {}".format(e, param))
