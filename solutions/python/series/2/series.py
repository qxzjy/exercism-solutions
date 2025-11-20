def slices(series: str, slice: int) -> list[str]:
    """
    Given a string of digits, output all the contiguous substrings of
    length n in that string in the order that they appear.
    
    :param series: str - the string of digits.
    :param slice: int - the length of the slice.
    :return list[str] - the contiguous substrings of length n.
    """
    validate(series, slice)
    
    return [series[i:i + slice] for i in range(len(series) - slice + 1)]


def validate(series, slice):
    EVAL = {
        "slice == 0": "slice length cannot be zero",
        "slice < 1" : "slice length cannot be negative",
        "len(series) == 0": "series cannot be empty",
        "slice > len(series)": "slice length cannot be greater than series length"
    }
    
    for expression, message in EVAL.items():
        if eval(expression):
            raise ValueError(message)