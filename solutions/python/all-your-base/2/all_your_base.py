def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """ Convert a number from one base to another.
 
    :param input_base: int - the initial base of the number.
    :param digits: list[int] - the number in a list of digit formart.
    :param output_base: int - the base to convert the number to.
    :return: list[int] - the number converted in the output base.
    :raise ValueError: when the argument input base or ouput base is less than 2
                       or when a digit is negative or greater than the input base.
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    number, result = 0, []

    for index, digit in enumerate(reversed(list(digits))):
        if digit >= input_base or digit < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        number += digit*input_base**index

    if number == 0:
        return [0]

    while number > 0:
        result = [number % output_base] + result
        number //= output_base

    return result
    
    
    
