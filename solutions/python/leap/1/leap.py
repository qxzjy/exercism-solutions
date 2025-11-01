def leap_year(year: int) -> bool:
    """
    Determine if a year is a leap year or not.

    :param year: int - year to analyze.
    :return bool - is lear year ?
    """
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0
