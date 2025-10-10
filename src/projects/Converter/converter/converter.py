# Fix for Python 3.10+ compatibility with collections.Callable deprecation
import collections
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable

from dateutil.parser import parse


def transpose(csv_list):
    """
    Transpose a list of rows into a list of columns

    example:
       [['x', 3], ['y', 4], ['z', 5]]

    will become:
       [['x', 'y', 'z'], [3, 4, 5]]

    :return: a transposed list of list
    """
    transposed = map(list, zip(*csv_list))

    return list(transposed)


def string_to_date(string):
    """
    The date returned is a datetime.datetime object

    No need to specify the format:
    date.year gives the year
    date.month gives the month
    date.day gives the day

    the '.date()' remove the hours.

    :param string:
    :return: the date
    """
    return parse(string).date()


def string_to_float(string):
    """
    return a float from a string

    :param string:
    :return: float
    """
    return float(string)
