"""EX02 - One Shot Wordle."""

__author__ = "730515426"

secret_word: str = "python"
user_word: str = input("What is your 6-letter guess? ")
while len(user_word) != 6:
    user_word = input("That was not 6 letters! Try again: ")
if len(user_word) == 6:
    if user_word == secret_word:
        print("Woo! You got it! ")
    else:
        print("Not quite. Play again soon! ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

word_idx: int = 0
emoji_str: str = ""

while word_idx < len(secret_word):
    if user_word[word_idx] == secret_word[word_idx]:
        emoji_str += GREEN_BOX
        word_idx += 1
    else:
        emoji_str += WHITE_BOX
        word_idx += 1

print(emoji_str)