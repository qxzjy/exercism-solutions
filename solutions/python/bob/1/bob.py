def response(hey_bob: str) -> str:
    """
    Determine Bob's answer depending on the sentence.
 
    :param sentence: str - sentence to analyze.
    :return str - Bob's answer.
    """
    sentence = hey_bob.strip()

    if not sentence :
        return "Fine. Be that way!"
    elif sentence.endswith("?"):
        if sentence.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    elif sentence.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
