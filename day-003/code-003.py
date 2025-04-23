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

#####

SHOWS = [
    "  Avater: The last Airbender",
    "ben 10",
    "arthur",
    "   spongebob Square pants",
    "phineas and ferb",
    "Kim possible  ",
    "Jimmy Neutron  ",
    "The proud family"
]

def main():
    for show in SHOWS:
        print(show.strip().title())

main()
#Output:
"""
Avater: The Last Airbender
Ben 10
Arthur
Spongebob Square Pants
Phineas And Ferb
Kim Possible
Jimmy Neutron
The Proud Family
"""

#####
def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
    print(cleaned_shows)

main()

# Output:
#['Avater: The Last Airbender', 'Ben 10', 'Arthur', 'Spongebob Square Pants', 'Phineas And Ferb', 'Kim Possible', 'Jimmy Neutron', 'The Proud Family']


#####
def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
    
    print(", ".join(cleaned_shows))

main()

# Output:
# Avater: The Last Airbender, Ben 10, Arthur, Spongebob Square Pants, Phineas And Ferb, Kim Possible, Jimmy Neutron, The Proud Family


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
