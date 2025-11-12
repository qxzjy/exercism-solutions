ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rows(letter: str) -> list[str]:
    """ Draw a diamond for a specific letter.
 
    :param letter: str - the letter for which we want to draw a diamond.
    :return: list[str] - the diamond drawn.
    """
    letters = [chr(k) for k in range(ord("A"), ord(letter) + 1)]
    alphabet = letters[:-1] + letters[::-1]
    diamond_line = letters[::-1] + letters[1:]
    
    return ["".join(x if x == y else " " for y in diamond_line) for x in alphabet]
