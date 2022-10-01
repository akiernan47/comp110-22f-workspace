"""EX06 - Adventure."""

__author__ = "730515426"


player: str = ""
points: int = 0
def main() -> None:
    greet()
    print(player)


def greet() -> None:
    print("Welcome to the number guessing game! ")
    global player
    player = input("Enter your name: ")
    
    


if __name__ == "__main__":
  main()