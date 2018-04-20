""" Parametrized test cases
https://eli.thegreenplace.net/2011/08/02/python-unit-testing-parametrized-test-cases
https://pastebin.com/rdMqXc7b
https://stackoverflow.com/questions/5068100/how-to-factorise-python-test-cases-with-nosetests
https://technomilk.wordpress.com/2012/02/12/multiplying-python-unit-test-cases-with-different-sets-of-data/
https://stackoverflow.com/questions/17260469/instantiate-python-unittest-testcase-with-arguments
"""

import unittest


# Example 1 with test suite

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite


class TestOne(ParametrizedTestCase):
    """ test One """

    def test_something(self):
        """ test ex2 """
        # print('param =', self.param)
        self.assertEqual(1, 1)

    def test_something_else(self):
        """ test ex2 """
        self.assertEqual(2, 2)


suite = unittest.TestSuite()
suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=42))
suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=13))
unittest.TextTestRunner(verbosity=2).run(suite)


# Example 2 with class factory

def make_case(param):
    """ make test case factory """

    class MyTestCase(unittest.TestCase):
        """ test case factory """

        def test_foo(self):
            """ test example """
            self.assertEquals(param, 1)

    return MyTestCase


class ConcreteTestCase(make_case(1)):
    """ test class with parameter """
    pass


# Example 3 using class attributes
class TestOdd9(unittest.TestCase):
    """ test odd 1 """
    NUMBER = 9

    def runTest(self):
        """Assert that the item is odd"""
        self.assertTrue(self.NUMBER % 2 == 1, "Number should be odd")


class TestOdd7(TestOdd9):
    """ test odd 2 """
    NUMBER = 7


# Example 4 using multiple inheritance

def func_odd(_, n):
    """ Function ODD for test """

    # print(n)

    if n % 2 == 1:
        return True
    else:
        return False


class ClassOdd:
    """ bogus class"""

    def f_odd(self, n):
        """ Function ODD for test """

        # print(n)

        if n % 2 == 1:
            return True
        else:
            return False


class TestOdd:
    """ test odd with nosetest"""

    def runTest(self):
        """Assert that the item is odd"""
        self.assertTrue(self.NUMBER % 2 == 1, "Number should be odd")
        self.assertTrue(self.func(3))
        self.assertTrue(self.f(5))


class TestOdd3(TestOdd, ClassOdd, unittest.TestCase):
    """ test odd 3 """
    NUMBER = 3
    func = func_odd
    f = ClassOdd.f_odd


class TestOdd5(TestOdd, ClassOdd, unittest.TestCase):
    """ test odd 4 """
    NUMBER = 5
    func = func_odd
    f = ClassOdd.f_odd


# Example 5 using abstract class

def function_a(string):
    """ bogus True """
    print(string)
    return True


def function_b(string):
    """ Bogus True """
    print(string)
    return True


class AbstractTestCase:

    def test_generic_input_one(self):
        result = self.function("input 1")
        self.assertTrue(result)

    def test_generic_input_two(self):
        result = self.function("input 2")
        self.assertTrue(result)


class TestsFunctionA(AbstractTestCase, unittest.TestCase):

    def function(self, param):
        return function_a(param)

    def test_specific_input(self):
        self.assertTrue(self.function("specific input"))


class TestsFunctionB(AbstractTestCase, unittest.TestCase):

    def function(self, param):
        return function_b(param)

    def test_another_specific_input(self):
        self.assertTrue(self.function("another specific input"))


if __name__ == '__main__':
    unittest.main()
