def is_valid(isbn: str) -> bool:
    """
    Determine if a ISBN-10 is valid.
 
    :param isbn: str - the ISBN to analyze.
    :return: bool - is the ISBN valid ?
    """
    chars = list(isbn.replace("-", ""))

    if chars and chars[-1] == "X":
        chars[-1] = "10"
    
    if not len(chars) == 10 or not all(char.isdigit() for char in chars):
        return False

    return not sum(int(char) * index for index, char in zip(range(10, 0, -1), chars)) % 11
