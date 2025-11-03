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
    result = ""
    
    if not number % 3:
        result += "Pling"
        
    if not number % 5:
        result += "Plang"
        
    if not number % 7:
        result += "Plong"

    return result or str(number)