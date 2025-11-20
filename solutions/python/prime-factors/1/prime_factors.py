def factors(value: int) -> list[int]:
    """
    Compute the prime factors of a given natural number.
 
    :param value: int - the natural number.
    :return list[int] - the list of prime factors.
    """
    factor = 2
    factors = list()

    while value > 1:
        if not value % factor:
            factors.append(factor)
            value /= factor
        else:
            factor += 1

    return factors