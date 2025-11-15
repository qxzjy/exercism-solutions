def square_of_sum(number: int) -> int:
    """
    Determine the square of sum of the first x natural numbers.
 
    :param number: int - the first natural numbers.
    :return: int - the square of sum.
    """
    
    return sum(range (1, number+1))**2


def sum_of_squares(number: int) -> int:
    """
    Determine the sum of squares of the first x natural numbers.
 
    :param number: int - the first natural numbers.
    :return: int - the sum of squares.
    """
    
    return sum(i**2 for i in range (1, number+1))


def difference_of_squares(number: int) -> int:
    """
    Determine the difference between the square of sum and the sum
    of squares of the first x natural numbers.
 
    :param number: int - the first natural numbers.
    :return: int - difference between the square of sum and the sum
    of squares.
    """
    
    return square_of_sum(number) - sum_of_squares(number)
