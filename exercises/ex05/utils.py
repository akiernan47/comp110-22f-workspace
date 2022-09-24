"""ex05 - More List Utils."""

__author__ = "730515426"


def only_evens(given_list: list[int]) -> list[int]:
    """Returns new list only containing even elements."""
    i: int = 0
    evens_list: list[int] = [] 
    if len(given_list) == 0:
        return evens_list
    while i < len(given_list):
        if given_list[i] % 2 == 0:
            evens_list.append(given_list[i])
            i += 1
        else:
            i += 1
    return evens_list


def concat(ints_one: list[int], ints_two: list[int]) -> list[int]:
    """Returns new list containing all elements of the two lists."""
    concat_list: list[int] = []
    one_i: int = 0
    two_i: int = 0
    while one_i < len(ints_one):
        concat_list.append(ints_one[one_i])
        one_i += 1
    while two_i < len(ints_two):
        concat_list.append(ints_two[two_i])
        two_i += 1
    return concat_list


def sub(given_list: list[int], start: int, end: int) -> list[int]:
    """Returns subset of a list based on given start and end value."""
    sub_list: list[int] = []
    if len(given_list) == 0 and start > len(given_list) or end <= 0:
        return sub_list
    elif end > len(given_list):
        end = len(given_list)
    elif start < 0:
        start = 0
    while start < end:
        sub_list.append(given_list[start])
        start += 1
    return sub_list
