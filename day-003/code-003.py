# DAY 3 - 17/04/2025
#CS50P: Introduction To Programming with Python
#SHORTS

### STRING EFFECTS:

def main():
    guess = int(get_guess())

    if guess == 50:
        print("Correct!")

    else:
        print("Incorrect!")

def get_guess():
    guess = input("Enter a guess: ")
    return guess

main()


### SIDE EFFECT:

emoticon = ":("

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Hi there!")

def say(phrase):
    print(phrase + " " + emoticon)

main

#Output:
# Is anyone there? :(
# Ho there! :D
