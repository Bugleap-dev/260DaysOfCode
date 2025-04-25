# DAY 007 - 21/04/2025
# CS50P: Introduction To Programming with Python

# LECTURE 1 -CONDITIONALS

#SHORTS - CONDITIONALS

def main():
    players = input("Multiplayer or Single-player: ")
    difficulty = input("Difficult or Easy")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondike")
        else:
            print("Enter a valid number of players: ")
            

    elif difficulty == "Easy":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Caasual":
            recommend("Clock")
        else:
            print("Enter a valid number of players: ")
    

def recommend(game):
    print(f"You might like, {game}")

    
main()

##############
def main():
    players = input("Multiplayer or Single-player: ")
    if not (players == "Multiplayer" or "Single-player"):
        print("Enter a valid number of player ")
        return
    
    difficulty = input("Difficult or Easy: ")
    if not (difficulty == "Difficult" or "Easy"):
        print("Enter a valid difficulty ")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Sinle-player":
        recommend("Klondike")
    elif difficulty == "Easy" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")
        

def recommend(game):
    print(f"You might like, {game}")


main()

