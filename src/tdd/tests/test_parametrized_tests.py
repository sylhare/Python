""" Parametrized test cases
https://eli.thegreenplace.net/2011/08/02/python-unit-testing-parametrized-test-cases
https://pastebin.com/rdMqXc7b
"""

import unittest


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
        print('param =', self.param)
        self.assertEqual(1, 1)

    def test_something_else(self):
        self.assertEqual(2, 2)


def make_case(x):
    class MyTestCase(unittest.TestCase):
        def test_foo(self):
            self.assertEquals(x, 1)

    return MyTestCase


class ConcreteTestCase(make_case(1)):
    pass


suite = unittest.TestSuite()
suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=42))
suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=13))
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    unittest.main()