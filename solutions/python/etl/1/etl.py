def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """
    Transform a dictionnary from a format to another.

    Before : {1: ["A", "E", "I", "O", "U"]}
    After : {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
 
    :param legacy_data: dict[int, list[str]] - the dictionnary to transform.
    :return: dict[str, int] - the dictionnary transformed.
    """
    data = dict()
    
    for key, value in legacy_data.items():
        for letter in value:
            data[letter.casefold()] = key

    return data
