
class Calculator(object):

    def add(self, x, y):
        number_types = (int, long, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

    def factorial(self, number):
        number = int(number)
        if (number == 0) or (number == 1):
            return 1
        else:
            return number * self.factorial(number - 1)
