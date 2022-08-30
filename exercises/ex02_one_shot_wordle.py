"""EX02 - One Shot Wordle."""

__author__ = "730515426"

secret_word: str = "python"
secret_len: int = len(secret_word)

# Prompting user to input their guess of the secret word as a variable of the string type
user_word: str = input(f"What is your {secret_len}-letter guess? ")
# Executes while the guess does not match the length of the secret word for error checking
while len(user_word) != secret_len:
    user_word = input(f"That was not {secret_len} letters! Try again: ")

# Named constants for the relevant box colors used in the program:
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Will keep track of the index of a string, initialized at first position ([0])
idx: int = 0
# Will store the corresponding box colors as a string, initialized at empty status
emoji_str: str = ""

# Executes while the index value is less than the length of the secret word:
while idx < secret_len:
    # Checks for match of a character at a given index for the guess and secret
    # If match present:
    if user_word[idx] == secret_word[idx]:
        emoji_str += GREEN_BOX
        idx += 1
    # If match not present:
    else:
        chr_present: bool = False  # Initializes variable for a character existing at False
        altidx: int = 0  # Initializes variable to hold alternative indexes of the secret word
        
# Loop runs while character is not present and the other index is below the secret length
        while not chr_present and altidx < secret_len:
            if secret_word[altidx] == user_word[idx]:
                chr_present = True  
                # Character listed as existing somewhere else in the secret word
            else:
                altidx += 1  # Count increased by one for the next iteration of the loop 
        if chr_present:
            emoji_str += YELLOW_BOX  # Corresponding box output for a present character
            idx += 1  # Increase count for the scope of the outer loop
        else:
            emoji_str += WHITE_BOX  # Corresponding box output for a non-present character
            idx += 1  # Increase count for the scope of the outer loop
        
print(emoji_str)  
# Complete string of the length of the secret word is output(comprised of boxes)

# Final guess checking conditional:
if len(user_word) == secret_len:
    if user_word == secret_word:
        print("Woo! You got it! ")  # Correct response
    else:
        print("Not quite. Play again soon! ")  # Incorrect response