from lettuce import *
from nose.tools import assert_equals
from app.calculator import Calculator


@step(u'I am using the calculator')
def select_calc(step):
    """

    :param step:
    """
    print('Attempting to use calculator...')
    world.calc = Calculator()


@step(u'I input "([^"]*)" add "([^"]*)"')
def given_i_input_group1_add_group1(step, x, y):
    """

    :param step:
    :param x:
    :param y:
    """
    world.result = world.calc.add(int(x), int(y))


@step(u'I should see "([^"]+)"')
def result(step, expected_result):
    """

    :param step:
    :param expected_result:
    """
    actual_result = world.result
    assert_equals(int(expected_result), actual_result)


@step('I have the number (\d+)')
def have_the_number(step, number):
    """

    :param step:
    :param number:
    """
    world.number = int(number)


@step('I compute its factorial')
def compute_its_factorial(step):
    """

    :param step:
    """
    world.number = world.calc.factorial(world.number)


@step('I see the number (\d+)')
def check_number(step, expected):
    """

    :param step:
    :param expected:
    """
    expected = int(expected)
    assert world.number == expected, \
        "Got %d" % world.number



