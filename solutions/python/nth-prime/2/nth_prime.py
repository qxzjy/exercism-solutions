from collections.abc import Generator, Iterator
from itertools import islice, count
from functools import cache

def prime(number: int) -> int:
    """ Given a number n, determine what the nth prime is.
 
    :param number: int - the number.
    :return int - the nth prime.
    """
    if number == 0:
        raise ValueError('there is no zeroth prime')
        
    gen = islice(filter(is_prime, count(2)), number)
    
    for _ in range(number - 1): next(gen)
        
    return next(gen)


@cache
def is_prime(counter: Iterator) -> Generator[int, None, None]:
    
    return all(counter % test != 0 for test in range(2, int(counter ** 0.5) + 1))