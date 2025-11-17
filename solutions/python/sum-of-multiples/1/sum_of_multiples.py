def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """
    Determine the sum of multiples considering a specific limit.
 
    :param limit: int - the limit.
    :param multiples: list[int] - the multiples.
    :return: list[str] - the sum of the unique multiples.
    """
    return sum(set(index for multiple in multiples if multiple for index in range(multiple, limit, multiple)))
            
        
