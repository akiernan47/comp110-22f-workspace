"""ex05 - More List Utils."""

__author__ = "730515426"

def only_evens(given_list: list[int]) -> list[int]:
    """Returns new list only containing even elements"""
    i: int = 0
    evens_list: list[int] = []  # Initialize empty list
    # If the list is empty:
    if len(given_list) == 0:
        return evens_list
    
    # Loop will check each index for an even character
    while i < len(given_list):
        if given_list[i] % 2 == 0:
            evens_list.append(given_list[i])  # Appends even int to new list
            i += 1
        else:
            i += 1
    return evens_list  # Returns list of even ints found in the given list
