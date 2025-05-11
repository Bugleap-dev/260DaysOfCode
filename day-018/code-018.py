

# SHORTS: LISTS

results = ["Mario", "Luigi",]
results.append("Yoshi")
print(results)                                # Output: ['Mario', 'Luigi', 'Yoshi']

#################

results.append(["Princess","Bowser"])         # .append(): Adds an item (a single item) to the end of the list.

print(results)                                # Output: ['Mario', 'Luigi', 'Yoshi', ['Princess', 'Bowser']]

####################

results.remove(["Princess","Bowser"])         # .remove(): remove the first item stated.

results.extend(["Princess","Bowser"])         # .extend(): Extends the list by appending elements from the iterable.

print(results)                                # Output: ['Mario', 'Luigi', 'Yoshi', 'Princess', 'Bowser']

print(results[3])                             # Output: Princess

##########################

results = [
    'Mario', 'Luigi', 'Yoshi', 'Mario', 'Princess', 'Bowser', 'Koopa Troopa', 'Toad'
    ]
results.remove("Mario")

print(results)                               # Output: ['Luigi', 'Yoshi', 'Mario', 'Princess', 'Bowser', 'Koopa Troopa', 'Toad']

##############

results.insert(3,"Donkey Kong Jnr.")        # Insert Donkey Kong Jnr. at index 3
print(results)
# Output:['Luigi', 'Yoshi', 'Mario', 'Donkey Kong Jnr.', 'Princess', 'Bowser', 'Koopa Troopa', 'Toad']

###############

results = [
    'Luigi', 'Yoshi', 'Mario', 'Donkey Kong Jnr.', 'Princess', 'Bowser', 'Koopa Troopa', 'Toad'
    ]

results.reverse()                           # .reverse(): Reverses the elements in place.
print(results)
#Output: ['Toad', 'Koopa Troopa', 'Bowser', 'Princess', 'Donkey Kong Jnr.', 'Mario', 'Yoshi', 'Luigi']

#########################

# SHORTS: List and Dictionary Comprehensions

def main():
    words = "address.txt"
    lowercase_word = [word.lower() for word in words if len(word) > 4]

    counts = {word: words.count(word) for word in lowercase_word}


    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1    
    
    
main()

#########################

# SHORTS: LIST METHOD


def main():
    history = []

    while True:
        action = input("Action: ")

        if action.lower() == "undo":
            undone = history.pop()
            print(f"Undone: {undone}")
        
        elif action.lower() == "restart":
            history.clear()
            print(history)
        
        elif action.lower() == "done":
            history.pop()
            break

        else:
            history.append(action)
            print(history)

main()

##################

# SHORTS: STRING METHODS

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

#################

# SHORTS: STRING SLICING

def main():

    phone = "617-495-1000"
    print(phone[0:3])       # [0:3] => prints the string starting from the 0th index and stopping before the 3rd index.
    # Output: 617

    print(phone[:3])        # [:3] => prints the string starting from the 0th index and stopping before the 3rd index
    # Output: 617

    print(phone[8:12])      # [8:12] => prints the string starting from the 8th index and stopping before the 12rd index
    # Output: 1000

    print(phone[8:])        # [8:] => prints the string starting from the 0th index and stopping before the 3rd index
    # Output: 1000

    print(phone[-4:])       # [-4:] => prints the string starting from the right hand side of 4 indexes.
    # Output: 1000


main()