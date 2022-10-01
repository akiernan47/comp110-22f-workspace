"""EX06 - Adventure."""

__author__ = "730515426"


player: str = ""
points: int = 0


def main() -> None:
    """Will drive the program."""
    greet()
    play: bool = True
    while play:
        print(f"\n Current points: {points}")
        choice: str = input(" \n 1. Custom procedure \n 2. Custom Function \n 3. Quit \n Desired option: ")
        if choice == "1":
            print("1 done")
        elif choice == "2":
            print("2")
        elif choice == "3":
            print("3")
            play = False
        else:
            print("nada")
            choice = input(" \n 1. Custom procedure \n 2. Custom Function \n 3. Quit \n Desired option: ")
    
    
 



def greet() -> None:
    """Greets user and prompts for their name."""
    print("Welcome to the number guessing game! ")
    global player
    player = input("Enter your name: ")


if __name__ == "__main__":
    main()