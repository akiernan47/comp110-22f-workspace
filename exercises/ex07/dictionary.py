"""Dictionary Functions."""

__author__ = "730515426"


def invert(initial: dict[str, str]) -> dict[str, str]:
    reverse = {}
    for key in initial:
        value = initial[key]
        reverse[value] = key
    if len(reverse) != len(initial):
        raise KeyError
    else:
        return reverse
        
    
    

print(invert({"1": "2", "3": "4"}))
print(invert({"1": "2", "3": "2"}))

