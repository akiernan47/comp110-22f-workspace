"""EX04 - List Utils."""

__author__ = "730515426"


def all(list_input: list[int], given_int: int) -> bool:
    """Will search list of ints and determine whether they all match a given int."""
    i: int = 0
    # When the list is empty:
    if len(list_input) == 0:
        return False
    
    # Loop will check each index of the list for a match to the given int
    while i < len(list_input):
        if given_int == list_input[i]:
            i += 1
        else:
            return False
    return True


def max(list_input: list[int]) -> int:
    """Returns the largest item in a given list."""
    # When the list is empty:
    if len(list_input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max_num: int = list_input[i]

    # Loop will compare each int in the list to the previously highest int and return the maximum
    while i < len(list_input):
        if max_num < list_input[i]:
            max_num = list_input[i]
        i += 1
    return max_num


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Determines if two lists exhibit deep equality."""
    i: int = 0
    
    if len(list_one) == len(list_two):
        # Loop will check for a match at the same indexes for every item in the two lists
        while i < len(list_one):
            if list_one[i] == list_two[i]:
                i += 1
            else:
                return False  # No deep equality
        return True  # Deep equality
    return False  # List lengths do not match, so cannot exhibit deep equality