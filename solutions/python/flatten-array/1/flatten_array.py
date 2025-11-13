def flatten(iterable: list[list]) -> list[int]:
    """ Flatten a nested array of any depth.
 
    :param word: list[list] - the nested array.
    :return: list[int] - the nested array flatten.
    """
    iterable_flatten = []
    
    for item in iterable:
        if isinstance(item, list):
            iterable_flatten.extend(flatten(item))
        elif item is not None:
            iterable_flatten.append(item)
        
    return iterable_flatten