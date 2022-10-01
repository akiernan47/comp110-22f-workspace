"""EX06 - Adventure."""

__author__ = "730515426"


player: str = ""
points: int = 0


def main() -> None:
    """Will drive the program."""
    greet()
    global points
    play: bool = True
    while play: 
        print(f"\n Current points: {points}")
        choice: str = input(" \n 1. Learn the rules & gain points \n 2. Real Game \n 3. Quit \n Desired option: ")
        if choice == "1":
            print("1 done")
        elif choice == "2":
            print("2 done")
        elif choice == "3":
            print(f"\n Accumulated points: {points} \n Thanks for playing {player}")
            play = False
        else:
            print("Invalid option, please choose again. \n")
            
    
def greet() -> None:
    """Greets user and prompts for their name."""
    print("Welcome to the number guessing game! ")
    global player
    player = input("Enter your name: ")


def practice() -> None:
    """Allows user to gain points through guessing game."""


if __name__ == "__main__":
    main()