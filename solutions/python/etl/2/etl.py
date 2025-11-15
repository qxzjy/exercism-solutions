def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """
    Transform a dictionnary from a format to another.

    Before : {1: ["A", "E", "I", "O", "U"]}
    After : {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
 
    :param legacy_data: dict[int, list[str]] - the dictionnary to transform.
    :return: dict[str, int] - the dictionnary transformed.
    """

    return {val.lower(): key for key in legacy_data.keys() for val in legacy_data[key]}