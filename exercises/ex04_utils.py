"""EX04 - List Utils."""

__author__ = "730515426"


def all(int_list: list[int], given_int: int) -> bool:
    """Will search list of ints and determine whether they all match a given int."""
    i: int = 0
    nums: list[int] = list(int_list)
    if len(nums) == 0:
        return False
    while i < len(nums):
        if given_int == nums[i]:
            i += 1
        else:
            return False
    return True
        