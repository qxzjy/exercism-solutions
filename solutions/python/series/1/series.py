def slices(series: str, length: int) -> list[str]:
    """
    Given a string of digits, output all the contiguous substrings of
    length n in that string in the order that they appear.
    
    :param series: str - the string of digits.
    :param length: int - the length.
    :return list[str] - the contiguous substrings of length n.
    """
    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if not series:    
        raise ValueError("series cannot be empty")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    return [series[i:i+length] for i in range(0, len(series)-length+1)]