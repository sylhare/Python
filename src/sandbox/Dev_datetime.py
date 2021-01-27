from datetime import datetime


def is_leap(year):
    """
    In the Gregorian calendar, three conditions are used to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless:
        The year can be evenly divided by 100, it is NOT a leap year, unless:
            The year is also evenly divisible by 400. Then it is a leap year.

    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == "__main__":  # pragma: no cover
    """
    https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime
    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    """
    datetime.strptime('24052010', "%d%m%Y").date()
    datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
