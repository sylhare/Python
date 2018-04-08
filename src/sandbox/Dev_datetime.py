from datetime import datetime


if __name__ == "__main__":  # pragma: no cover
    """
    https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime
    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    """
    datetime.strptime('24052010', "%d%m%Y").date()
    datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
