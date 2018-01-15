class Calculator(object):

    def add(self, x, y):
        number_types = (int, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

    def bugged_add(self, x, y):
        """Which actually does a substraction, adding prints to detect the error"""
        number_types = (int, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            print ('X is: {}'.format(x))
            print ('Y is: {}'.format(y))
            result = x - y
            print ('Result is: {}'.format(result))
            return result
        else:
            raise ValueError

    def bugged_add_with_pdb(self, x, y):
        number_types = (int, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            import pdb;
            pdb.set_trace()
            return x - y
        else:
            raise ValueError


