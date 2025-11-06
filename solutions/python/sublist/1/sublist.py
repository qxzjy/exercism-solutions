"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
UNEQUAL = 0
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3

def sublist(list_one: list[int], list_two: list[int]) -> str:
    """
    Compare if two lists are equal, unequal, sublist or superlist.
    
    :param list_one: list[int] - first list to analyze.
    :param list_two: list[int] - second list to analyze.
    :return str - the list comparaison ["EQUAL" | "UNEQUAL" | "SUBLIST" | "SUPERLIST"].
    """
    if list_one == list_two:
        return 3
    elif is_sublist(list_one, list_two):
        return 2
    elif is_sublist(list_two, list_one):
        return 1

    return 0

def is_sublist(list_one: list[int], list_two: list[int]) -> bool:
    """
    Compare if a list is a sublist of another.
 
    :param list_one: list[int] - first list to analyze.
    :param list_two: list[int] - second list to analyze.
    :return bool - True if list_one is a sublist of list_two, else False.
    """
    for i in range(len(list_one) - len(list_two) + 1):
        if not list_two or list_two == list_one[i : i + len(list_two)]:
            return True
    
    return False