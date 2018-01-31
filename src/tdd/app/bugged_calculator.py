class BuggedCalculator(object):
    """ A calculator that does not work """

    def bugged_add(self, x, y):
        """Which actually does a subtraction, adding prints to detect the error"""
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
        """ Add fonction that does not work for testing purpose """
        number_types = (int, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            # import pdb; # To investigate the error
            # pdb.set_trace()
            return x - y
        else:
            raise ValueError