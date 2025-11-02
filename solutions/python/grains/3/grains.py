def square(number: int) -> int:
    """
    Determine the number of grains on a given square.
 
    :param number: int - the number of the square.
    :return int - number of grains on a given square.
    :raise ValueError: when the argument number is not in the acceptable range [1, 64]
    """
    if number not in range(1,65):
        raise ValueError("square must be between 1 and 64")
        
    return 2**(number-1)


def total() -> int:
    """
    Determine the total number of grains on the chessboard.
 
    :return int - total number of grains on the chessboard.
    """
    return 2**64-1
