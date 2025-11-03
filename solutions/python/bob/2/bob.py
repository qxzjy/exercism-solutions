def response(hey_bob: str) -> str:
    """
    Determine Bob's answer depending on the sentence.
 
    :param sentence: str - sentence to analyze.
    :return str - Bob's answer.
    """
    sentence = hey_bob.strip()
    is_capitalized = sentence.isupper()
    is_question = sentence.endswith('?')

    if not sentence:
        return "Fine. Be that way!"
    elif is_question:
        if is_capitalized:
            return "Calm down, I know what I'm doing!"
        return "Sure."
    elif is_capitalized:
        return "Whoa, chill out!"
    else:
        return "Whatever."
