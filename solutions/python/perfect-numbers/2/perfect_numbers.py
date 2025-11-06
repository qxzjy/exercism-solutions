def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    :raise ValueError: when the argument number is not a positive integers.
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")  
        
    aliquot_sum = sum([divisor for divisor in range (1, number//2+1) if not number % divisor])
    

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
