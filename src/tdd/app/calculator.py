class Calculator(object):

    def add(self, x, y):
        number_types = (int, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

    def subtract(self, a, b):
        """

        :param b:
        :return:
        """
        return a - b

    def multiply(self, a, b):
        """

        :param b:
        :return:
        """
        return a * b

    def divide(self, a, b):
        """

        :param b:
        :return:
        """
        return a * 1.0 / b
