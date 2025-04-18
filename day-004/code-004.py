## DAY 004 - 18/04/2025
# CS50P: Introduction To Programming with Python**

# LECTURE 1 -CONDITIONALS

###

#IF:
x = int(input("What's x? "))        #Output: What's x? 3
y = int(input("What's y? "))        #Output: What's y? 5

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

##Output: x is less than y

########
# OR:
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

######

x = int(input("What's x? "))
y = int(input("What's y? "))

if x!=y:
    print("x is not equal to y")
else:
    print("X is equal to y")

######

greeting = greet("hello, computer")
print(greeting)
#Output 
# hello there


###
x = int(input("What's x?: "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

###
def main():
    x = int(input("What's x?: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")        


def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False
    
main()

#
def main():
    x = int(input("What's x?: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")        


def is_even(n):
    return True if n % 2 == 0 else False

main()

#
def main():
    x = int(input("What's x?: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")        


def is_even(n):
    return n % 2 == 0

main()

#
name = input("What's your name: ")
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Griffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

##
name = input("What's your name: ")
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

##
##
name = input("What's your name: ")
match name:
    case "Harry"|"Hermione"|"Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


########

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
    
    difficulty = input("Difficult or Easy")
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

