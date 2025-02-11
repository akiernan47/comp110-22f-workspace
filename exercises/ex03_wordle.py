"""EX03 - Structured Wordle."""

__author__ = "730515426"


def contains_char(searched_word: str, search_char: str) -> bool:
    """Will search for the presence of a character within a given string of any length."""
    assert len(search_char) == 1
    idx: int = 0  # Initialize index count to 0
    
    # Runs while the index count is below the length of the searched word
    while idx < len(searched_word):
        if searched_word[idx] == search_char:
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
    
    # Runs while the index count is below the length of the secret word
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


def input_guess(guess_len: int) -> str:
    """Will return a string (of an expected length) given by the user."""
    # Initial user prompt for a guess:
    secret_guess: str = input(f"Enter a {guess_len} character word: ")
    
    # Runs until the input is of an expected length:
    while len(secret_guess) != guess_len: 
        secret_guess = input(f"That wasn't {guess_len} chars! Try again: ")
    return secret_guess  # String with expected length is returned


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1  # Turn count initialized at 1
    secret: str = "codes"  # The secret the user is trying to guess
    guess: str = ""  # Initialize empty string to later hold user guess
    win = False  # Will become True if user guesses correctly
    
    # Runs while the user is between turn 1-6 and has not won
    while turn < 7 and not win:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))  # User input assigned to guess
        print(emojified(guess, secret))  # Prints emoji string
        turn += 1  # Increment turn by 1
        
        if secret == guess:
            win = True  # win condition
            print(f"You won in {turn - 1}/6 turns!")

    if not win:
        # Program response for loss
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
