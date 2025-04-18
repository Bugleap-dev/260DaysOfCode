# DAY 3 - 17/04/2025

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

##
