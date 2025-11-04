def is_pangram(sentence: str) -> bool:
    """
    Determine if a sentence is a pangram (contains every letter from the alphabet).
 
    :param sentence: str - the sentence to analyze.
    :return: bool - is the sentence a pangram ?
    """
    return len(set(char for char in sentence.lower() if char.isalpha())) == 26