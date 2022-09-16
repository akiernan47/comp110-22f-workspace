"""EX04 - List Utils."""

__author__ = "730515426"


def all(list_input: list[int], given_int: int) -> bool:
    """Will search list of ints and determine whether they all match a given int."""
    i: int = 0
    if len(list_input) == 0:
        return False
    while i < len(list_input):
        if given_int == list_input[i]:
            i += 1
        else:
            return False
    return True


def max(list_input: list[int]) -> bool:
    """returns the largest item in a given list."""
    if len(list_input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0

