def abbreviate(phrase: str) -> str:
    """
    Convert a phrase to its acronym.

    Punctuation is handled as follows: hyphens are word separators (like
    whitespace); all other punctuation can be removed from the input.
 
    :param phrase: str - the phrase to convert.
    :return str - the acronym of the phrase.
    """
    phrase_cleaned = "".join(filter(lambda x: x.isalpha() or x.isspace(), phrase.replace("-", " ")))

    return "".join([word[0].upper() for word in phrase_cleaned.split()])

