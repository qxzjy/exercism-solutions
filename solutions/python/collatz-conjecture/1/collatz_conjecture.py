def collatz_conjecture(number: int) -> int:
    """
    Apply the Collatz Conjecture for a given number.
 
    :param number: int - number we need to process.
    :return int - the number divided by 2 if even, else multiplicated by 3 and 1 added.
    """
    return number/2 if not number % 2 else number*3+1

def steps(number: int) -> int:
    """
    Determine how many steps it takes to reach 1 according to the rules
    of the Collatz Conjecture.
 
    :param number: int - number we need to process.
    :return int - number of steps to reach 1.
    :raise ValueError: when argument is zero or a negative integer.
    """
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    steps = 0

    while number != 1:
        number = collatz_conjecture(number)
        steps += 1
    
    return steps
