def is_isogram(sentence: str) -> bool:
    """
    Determine if a sentence is an isogram (contains no repeating letter).
 
    :param sentence: str - the sentence to analyze.
    :return: bool - is the sentence an isogram ?
    """
    char_only = [char.lower() for char in sentence if char.isalpha()]
    
    return len(set(char_only)) == len(char_only)