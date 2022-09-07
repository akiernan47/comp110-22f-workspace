"""EX03 - Structured Wordle."""

__author__ = "730515426"

"""Will search for the presence of a character (search_chr), within a given string of any length (searched_word)."""
def contains_char(searched_word: str, search_chr: chr) -> bool:
    assert len(search_chr) == 1
    idx: int = 0
    while idx < len(searched_word):
        if searched_word[idx] == search_chr:
            return True # Character is present
        else:
            idx += 1 
    return False # If loop completes, the chr has not been found in the word
    


