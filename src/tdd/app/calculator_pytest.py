
class Calculator(object):
    """ New calculator function to work with pytest """
    def __init__(self):
        self._last_answer = 0.0

    @property
    def last_answer(self):
        """

        :return:
        """
        return self._last_answer

    def _do_math(self, a, b, func):
        self._last_answer = func(a, b)
        return self.last_answer

    def add(self, a, b):
        return self._do_math(a, b, add)

    def subtract(self, a, b):
        return self._do_math(a, b, subtract)

    def multiply(self, a, b):
        return self._do_math(a, b, multiply)

    def divide(self, a, b):
        return self._do_math(a, b, divide)

    def maximum(self, a, b):
        return self._do_math(a, b, maximum)

    def minimum(self, a, b):
        return self._do_math(a, b, minimum)



def add(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a + b


def subtract(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a - b


def multiply(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a * b


def divide(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a * 1.0 / b


def maximum(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a if a >= b else b


def minimum(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a if a <= b else b
