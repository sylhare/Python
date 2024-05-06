"""
    Exception

"""

import os
import unittest


def not_found():
    """ raise FileNotFoundError """
    raise FileNotFoundError


class MyException(Exception):
    """ Custom exception """
    pass


class BetterException(Exception):
    """ Better exception """

    def __init__(self, msg=''):
        # self.msg = msg
        super(BetterException, self).__init__(msg)
        # log(msg)  # use your logging things here

    # def __str__(self):
    #     return self.msg


def my_function(path):
    """ add one to value """
    try:
        value = os.listdir(path)

        if value:
            raise MyException("Value is not null")

    except TypeError as e:
        print('the input should be a number {}'.format(e))
    except MyException as e:
        print(e)


def my_function_no_handling(path):
    """ no handling """
    try:
        value = os.listdir(path)

        if value:
            raise MyException("Value is not null")

    except TypeError as e:
        print('the input should be a number {}'.format(e))


def my_function_wrapper(path):
    """ wrapper """
    try:
        my_function_no_handling(path)
    except MyException as e:
        print("my custom error {}".format(e))


class Test(unittest.TestCase):
    @unittest.expectedFailure
    def test_not_found(self):
        self.assertRaises(FileNotFoundError, not_found())

    def test_function_typeError(self):
        self.assertRaises(TypeError, my_function(2))

    @unittest.expectedFailure
    def test_function_myException(self):
        with self.assertRaises(MyException):
            my_function(os.getcwd())

    def test_function_myException_again(self):
        print("[START]")
        try:
            my_function(os.getcwd())
        except MyException as err:
            print("{} {}".format(err.__class__, err))
        print("[END]")

    def test_function_nothandling_myException(self):
        with self.assertRaises(MyException):
            my_function_no_handling(os.getcwd())

    @unittest.expectedFailure
    def test_function_wrapper(self):
        with self.assertRaises(MyException):
            my_function_wrapper(os.getcwd())


if __name__ == "__main__":
    # my_function('str')
    unittest.main()

    print(' ----- here ----- ')
    try:
        raise BetterException('test')
    except BetterException as e:
        print(e)
