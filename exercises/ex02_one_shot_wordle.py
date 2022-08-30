"""EX02 - One Shot Wordle."""

__author__ = "730515426"

secret_word: str = "python"
secret_len: int = len(secret_word)
user_word: str = input(f"What is your {secret_len}-letter guess? ")
while len(user_word) != secret_len:
    user_word = input(f"That was not {secret_len} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

idx: int = 0
emoji_str: str = ""

while idx < secret_len:
    if user_word[idx] == secret_word[idx]:
        emoji_str += GREEN_BOX
        idx += 1
    else:
        chr_present: bool = False
        altidx: int = 0
        while not chr_present and altidx < secret_len:
            if secret_word[altidx] == user_word[idx]:
                chr_present = True
            else:
                altidx += 1
        if chr_present:
            emoji_str += YELLOW_BOX
            idx += 1
        else:
            emoji_str += WHITE_BOX
            idx += 1
        
print(emoji_str)

if len(user_word) == secret_len:
    if user_word == secret_word:
        print("Woo! You got it! ")
    else:
        print("Not quite. Play again soon! ")