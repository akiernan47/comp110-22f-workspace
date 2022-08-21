"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730515426"

user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

search_letter: str = input("Enter a single character: ")
if len(search_letter) != 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + search_letter + " in " + user_word)

chr_match_count: int = 0
if search_letter == user_word[0]:
    chr_match_count += 1
    print(search_letter + " found at index 0")

if search_letter == user_word[1]:
    chr_match_count += 1
    print(search_letter + " found at index 1")

if search_letter == user_word[2]:
    chr_match_count += 1
    print(search_letter + " found at index 2")

if search_letter == user_word[3]:
    chr_match_count += 1
    print(search_letter + " found at index 3")

if search_letter == user_word[4]:
    chr_match_count += 1
    print(search_letter + " found at index 4")

if chr_match_count > 0:
    if chr_match_count == 1:
        print("1 instance of " + search_letter + " found in " + user_word)
    else:
        print(str(chr_match_count) + " instances of " + search_letter + " found in " + user_word)
else:
    print("No instances of " + search_letter + " found in " + user_word)