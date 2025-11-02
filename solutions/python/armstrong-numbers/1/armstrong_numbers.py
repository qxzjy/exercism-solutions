def is_armstrong_number(number: int) -> bool:
    """
    Determine if a number is an armstrong number.

    An Armstrong number is a number that is the sum of its own 
    digits each raised to the power of the number of digits.
 
    :param number: int - the number to analyze.
    :return bool - is it an armstrong number ?
    """

    return number == sum([int(x)**len(str(number)) for x in str(number)])
        
