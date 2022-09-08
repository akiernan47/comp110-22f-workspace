"""EX03 - Structured Wordle."""

__author__ = "730515426"


def contains_char(searched_word: str, search_chr: str) -> bool:
    """Will search for the presence of a character within a given string of any length."""
    assert len(search_chr) == 1
    idx: int = 0  # Initialize index count to 0
   
    while idx < len(searched_word):
        if searched_word[idx] == search_chr:
            return True  # Character is present
        else:
            idx += 1 
    return False  # The character is not present within the word
    

# Named constants for emoji boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(secret_guess: str, secret: str) -> str:
    """Will return a string of emojis based on the accuracy of the user's guess."""
    assert len(secret_guess) == len(secret)
    idx: int = 0  # Initialize index count to 0
    emoji_str: str = ""  # Initialize empty string for eventual emoji output
    while idx < len(secret):
        if secret_guess[idx] == secret[idx]:
            emoji_str += GREEN_BOX  # Matching character at same index
            idx += 1
        elif contains_char(secret, secret_guess[idx]):
            emoji_str += YELLOW_BOX  # Character present at differing index
            idx += 1
        else:
            emoji_str += WHITE_BOX  # Non-present character
            idx += 1

    return emoji_str  # Completed string comprised of corresponding emojis


def input_guess(guess_len: int) -> int:
    secret_guess: str = input(f"What is your {guess_len}-letter guess? ")
    while len(secret_guess) != guess_len:
        user_word = input(f"That was not {guess_len} letters! Try again: ")
