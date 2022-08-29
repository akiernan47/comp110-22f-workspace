"""EX02 - One Shot Wordle"""

__author__ = "730515426"

secret: str = "python"
user_word: str = input("What is your 6-letter guess? ")
while len(user_word) != 6:
    user_word: str = input("That was not 6 letters! Try again: ")
if len(user_word) == 6:
    if user_word == secret:
        print("Woo! You got it! ")
    else:
        print("Not quite. Play again soon! ")
