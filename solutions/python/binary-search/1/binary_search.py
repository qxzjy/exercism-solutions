def find(search_list: list[int], value: int) -> int:
    """Find the index of a specific number in a list, using
    a binary search.
 
    :param search_list: list[int] - list of numbers.
    :param value: int - the number for which we want to know the index.
    :return: int - the index of the number.
    :raise ValueError: when the number is not in the inital list.
    """
    i = 0
    j = len(search_list) - 1
    
    while i <= j:
        mid = (i + j) // 2
        if value == search_list[mid]:
            return mid
        elif value < search_list[mid]:
            j = mid - 1
        else:
            i = mid + 1
    raise ValueError('value not in array')