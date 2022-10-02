"""EX06 - Adventure."""

__author__ = "730515426"

from random import randint

TROLL = "\U0001F9CC"
ANGEL = "\U0001F47C"
MAGE = "\U0001F9D9"
GRAVE = "\U0001FAA6"
LIGHTNING = "\U000026A1"
ALERT = "\U0001F6A8"
ANGUISHED = "\U0001F631"
player: str = ""
points: int = 0
troll_health: int = randint(10, 100)
troll_attack: int = randint(10, 100)
user_defense: int = 0
user_attack: int = 0


def main() -> None:
    """Will drive the program."""
    print()
    greet()
    global points
    play: bool = True
    while play: 
        print(f"\n{player}'s training points: {points}")
        print(f"{ALERT}{ALERT}{ALERT} Alert Carolina {ALERT}{ALERT}{ALERT}")
        print(f"Troll's {TROLL}  defense: {troll_health} & attack: {troll_attack}")
        print(f"{player}'s defense: {user_defense} & attack: {user_attack}")
        choice: str = input(" \n 1. Improve your skills \n 2. Test your might and face the beast \n 3. Throw in the towel and leave it to the UTAs (Quit) \n Desired option: ")
        if choice == "1":
            train()
            print(f"{player}'s defense: {user_defense} & attack: {user_attack}")
        elif choice == "2":
            points = encounter(points)
        elif choice == "3":
            print(f"\n A Comp 110 troll {TROLL}  still lingers... ")
            print(f"\n Accumulated training points (current life): {points} \n Thanks for playing {player}!")
            play = False
        else:
            print("Invalid option, please choose again. \n")
            
    
def greet() -> None:
    """Greets user and prompts for their name."""
    print(f"Oh no! An infamous COMP 110 troll is coming back to UNC, you must prepare to defeat it! {TROLL} ")
    print("You, yes you the user, is our only hope for salvation!")
    print("Luckily, ALERT Carolina will send out some information about the troll's power!")
    global player
    player = input("Enter your name brave venturer: ")


def train() -> None:
    """Allows user to gain points through training skills."""
    global points
    global user_defense
    global user_attack
    large_change: int = randint(30, 100)
    mid_change: int = randint(10, 30)
    small_change: int = randint(1, 10)
    neg_change: int = -100
    selection: str = input(f"\n{player}, do you want to improve your defense(1) or attack(2)? ")
    if selection == "1":
        print("1. Cybernetically enhance the durability of a body part\n2. Create a piece of armor from junkyard scraps\n3. Take notes on the defense of UNC's football team ")
        method_a: str = input(f"\n{player}, how will you improve your defense? ")
        if method_a == "1":
            user_defense += large_change
            points += large_change
            print("Great choice!")
        elif method_a == "2":
            user_defense += mid_change
            points += mid_change
            print("Alright choice")
        elif method_a == "3":
            user_defense += neg_change
            points += neg_change
            print(f"Why'd you pick that one? {ANGUISHED}")
        else:
            print("No stat improvement, invalid selection.")
    elif selection == "2":
        print("1. Receive instruction and equipment from the US Navy Seals \n2. Use the punching bag in your parent's basement for 5 minutes")
        method_d: str = input(f"\n{player}, how will you improve your attack? ")
        if method_d == "1":
            user_attack += large_change
            points += large_change
            print("Great choice!")
        elif method_d == "2":
            user_attack += small_change
            points += small_change
            print("Ok? As long as you're happy.")
        else:
            print("No stat improvement, invalid selection.")
    else:
        print("No stat improvement, invalid selection.")


def encounter(player_power: int) -> int:
    """Outlines different possibilities for the creature encounter."""
    global troll_health
    global troll_attack
    global user_defense
    global user_attack
    print()
    strategy: str = input(f"{player}, do you fight the troll {TROLL}  head-to-head (1) or use a surprise attack (2): ")
    if strategy == "1":
        if player_power > troll_health + troll_attack:
            print("Wohoo, you have vanquished the troll!! \nBut another one has appeared...")
            troll_health = randint(10, 100)
            troll_attack = randint(10, 100)
            return player_power
        else:
            print("The troll overpowers you in battle and strikes you down. You have been defeated.")
            print(f"An angel {ANGEL} has come to revive you! You come back to life at base stats.")
            user_defense = 0
            user_attack = 0
            player_power = 0
            return player_power
    elif strategy == "2":
        if user_attack > troll_health:
            print(f"You defeated the troll {TROLL}  in one swift blow, great job! \nUnfortunately, another troll has entered the fray")
            return player_power
        else:
            print(f"Your attack merely made a scratch, the troll {TROLL}  counters and defeats you")
            print(f"A mage {MAGE} approaches your body and uses a resurrection spell! You come back to life at base stats.")
            user_defense = 0
            user_attack = 0
            player_power = 0
            return player_power
    else:
        print(f"Due to your improper strategy, the troll {TROLL}  ambushed you. You have been defeated.")
        print(f"Your grave is struck by lightning {GRAVE}{LIGHTNING}, you come back to life at base stats.")
        user_defense = 0
        user_attack = 0
        player_power = 0
        return player_power


if __name__ == "__main__":
    main()