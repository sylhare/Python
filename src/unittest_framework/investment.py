#!/usr/bin/env python
# file: investment.py

import math

"""
Python 2.x
The invest module provides functions for calculating the total
interest payment on an investment.  
"""


def total_interest_continuously(principal, rate, time):
    """Returns the interest on the principal when invested at the given rate
    for the specified number of years.

    Note that the interest rate is expressed as a decimal
    >>> print round( total_interest_continuously( 1000, .12, 3 ), 2)
    433.33

    Different types are okay
    >>> print round( total_interest_continuously( 1000L, .12, 3 ), 2)
    433.33
    >>> print round( total_interest_continuously( 1000.00, .12, 3 ), 2)
    433.33

    When dividing to get the rate, make sure you don't get integer division
    >>> print round( total_interest_continuously( 1000L, 12/100., 3 ), 2)
    433.33

    Otherwise, you might not get what you expected
    >>> print round( total_interest_continuously( 1000L, 12/100, 3 ), 2)
    0.0

    For obscene amounts of time, the calculator overflows to infinity
    >>> print round( total_interest_continuously( 1000, .12, 30000 ), 2)
    inf

    If the principal is already equivalent to inf, the calculator degenerates to NAN.
    >>> print round( total_interest_continuously( 1.0e+1000000, .12, 3 ), 2)
    nan

    Negative interest rates are okay, but you'll get negative interest, of course.
    >>> print round( total_interest_continuously( 1000, -.12, 3 ), 2)
    -302.32

    >>> print round( total_interest_continuously( -1000, .12, 3 ), 2)
    Traceback (most recent call last):
    ...
    ValueError: Principal -1000.00 must be positive.

    >>> print round( total_interest_continuously( 1000, .12, -3 ), 2)
    Traceback (most recent call last):
    ...
    ValueError: Number of years -3.00 must be positive.

    No principal is okay, but the result it boring.
    >>> print round( total_interest_continuously( 0, .12, 3 ), 2)
    0.0

    Same with zero time.
    >>> print round( total_interest_continuously( 1000, .12, 0), 2)
    0.0
    """
    if principal < 0:
        raise ValueError("Principal %4.2f must be positive." % principal)
    if time < 0:
        raise ValueError("Number of years %3.2f must be positive." % time)
    return (principal * (math.e ** (rate * time))) - principal


def _test():
    """ Make the doc test"""
    import doctest, investment
    return doctest.testmod(investment)


if __name__ == '__main__':
    _test()