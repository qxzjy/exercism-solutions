def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """ Determine if a list of words are anagram of an other.
 
    :param word: str - the word for which we want to know if there are any anagrams.
    :param candidates: list[str] - the list of words to check.
    :return: list[str] - the list of words who are actually anagrams.
    """
    anagrams = list()

    for candidate in candidates:
        if word.lower() != candidate.lower() and sorted(word.lower()) == sorted(candidate.lower()):
            anagrams.append(candidate)
    
    return anagrams