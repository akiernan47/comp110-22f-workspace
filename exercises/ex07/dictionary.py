"""Dictionary Functions."""

__author__ = "730515426"


def invert(initial_dict: dict[str, str]) -> dict[str, str]:
    """Inverts dictionary's key-value pairs, raises error if any dupe keys."""
    reverse: dict[str, str] = {}
    for key in initial_dict:
        value = initial_dict[key]
        reverse[value] = key
    if len(reverse) != len(initial_dict):
        raise KeyError
    else:
        return reverse


def count(initial_list: list[str]) -> dict[str, int]:
    """Produces dictionary of how many times each list element is present."""
    counted_elems: dict[str, int] = {}
    for key in initial_list:
        if key in counted_elems:
            counted_elems[key] += 1
        else:
            counted_elems[key] = 1
    return counted_elems


def favorite_color(colors: dict[str, str]) -> str:
    """Returns most prevalent color from given dictionary as a string."""
    color_list: list[str] = []
    for color in colors:
        color_list.append(colors[color])
    prevalence: dict[str, int] = count(color_list)
    most_occurences: int = 0
    favorite: str = ""
    for color in prevalence:
        if prevalence[color] > most_occurences:
            most_occurences = prevalence[color]
            favorite = color
    return favorite