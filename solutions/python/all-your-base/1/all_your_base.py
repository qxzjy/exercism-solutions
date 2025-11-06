def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    
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
    
    
    
