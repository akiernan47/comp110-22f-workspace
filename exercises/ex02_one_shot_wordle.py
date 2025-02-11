"""EX02 - One Shot Wordle."""

__author__ = "730515426"

secret_word: str = "python"
secret_len: int = len(secret_word)

# Prompting user to input their guess of the secret word
user_word: str = input(f"What is your {secret_len}-letter guess? ")
# Executes while the length of the words do not match for error checking
while len(user_word) != secret_len:
    user_word = input(f"That was not {secret_len} letters! Try again: ")

# Named constants for the relevant box colors used in the program:
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Will keep track of the index of the guess string
idx: int = 0
# Will store the corresponding colored boxes as a string, initialized at empty status
emoji_str: str = ""

# Executes while the index value is less than the length of the secret word:
while idx < secret_len:
    # Checks for matching character at the same index for the user guess and secret word
    if user_word[idx] == secret_word[idx]:
        # Match at index | Green box added to the emoji string:
        emoji_str += GREEN_BOX  # Corresponding box output for character at a matching index
        idx += 1  # Look to the next index
    else:
        # No match at index:
        chr_present: bool = False  # Variable for a character's presence, initially False
        altidx: int = 0  # Initializes variable to hold alternative index of the secret word
        
# Loop runs while character is not present and the other index is less than the secret length
        while not chr_present and altidx < secret_len:
            # Checks for matching character at differing indexes for the guess and secret word
            if secret_word[altidx] == user_word[idx]:
                chr_present = True  
                # Character now listed as present within the secret word
            else:
                altidx += 1  # Look to the next alternative index for secret word
        if chr_present:
            # Yellow box added to the emoji string:
            emoji_str += YELLOW_BOX  # Corresponding box output for a present character
            idx += 1  # Look to the next index (jumps back to outer loop)
        else:
            # White box added to the emoji string:
            emoji_str += WHITE_BOX  # Corresponding box output for a non-present character
            idx += 1  # Look to the next index (jumps back to outer loop)
        
print(emoji_str)  # Complete emoji string is output

# Response output based on guess accuracy conditional:
if user_word == secret_word:
    print("Woo! You got it! ")  # Correct response
else:
    print("Not quite. Play again soon! ")  # Incorrect response