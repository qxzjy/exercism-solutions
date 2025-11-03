def convert(number: int) -> str:
    """
    Convert a number into a string.

    If :
    - divisible by 3, "Pling" is added to the result.
    - divisible by 5, "Pling" is added to the result.
    - divisible by 7, "Pling" is added to the result.
    Else :
    - the number as string.
 
    :param number: int - number we need to process.
    :return str - the converted number string.
    """
    sounds = {3: 'Pling',
              5: 'Plang', 
              7: 'Plong'}

    results = ''.join(sounds[divisor] for divisor in sounds.keys() if number % divisor == 0)

    return results or str(number)