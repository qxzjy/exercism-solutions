def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """ Determine if a list of words are anagram of an other.
 
    :param word: str - the word for which we want to know if there are any anagrams.
    :param candidates: list[str] - the list of words to check.
    :return: list[str] - the list of words who are actually anagrams.
    """
    
    return [
        candidate
        for candidate in candidates
        if candidate.casefold() != word.casefold()
        and sorted(candidate.casefold()) == sorted(word.casefold())
    ]