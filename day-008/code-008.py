# DAY 007 - 21/04/2025

# EXERCISE:
#Exercise 1: Temperature Converter

def main():
    temp = input("Enter temperature (Celsius to Fahrenheit and vice-versa): ")      #Receives input from user
    temp = temp.strip().lower()                                                             #Removes leading and trailing whitespaces

    if temp.endswith("c"):                                                          #If the user inputs a degree celsius or C
        celsius_replace = temp.lower().replace("°c", "").replace("c", "" )
        float_celsius = float(celsius_replace.strip())

        print(f"{float_celsius} Celsius is equal to {celsius_to_fahrenheit(float_celsius):.2f} Fahrenheit")

    elif temp.endswith("f"):
        fahrenheit_replace = temp.lower().replace("°f", "").replace("f", "" )
        float_fahrenheit = float(fahrenheit_replace.strip())

        print(f"{fahrenheit_to_celsius(float_fahrenheit):.2f} Fahrenheit is equal to {float_fahrenheit} celsius")
    else:
        print("Enter a degree in either celsius of fahrenheit!")

def celsius_to_fahrenheit(degree):
    return (degree * (9/5)) + 32

def fahrenheit_to_celsius(degree): 
    return (degree - 32) * (5/9)
    

main()

##################

#Exercise 2:  Tip Calculator

def main():
    meal = input("What is the total meal cost? ")
    percent = input("What percentage would you like to tip? ")
    people = float(input("How many people? ").strip())

    meal = meal.lower().strip().replace("$", "")
    float_meal = float(meal.strip())

    percent = percent.lower().strip().replace("%", "")
    float_percent = float(percent.strip())

    return_percent = percentage(float_percent)
    return_meal = meal_and_tip(float_meal,return_percent)
    return_splitting = split(return_meal,people)

    print(f"Each person should pay: $ {return_splitting:.2f}")


def percentage(amount):
    return amount / 100

def meal_and_tip(meal,tip):
    return (meal * tip) + meal

def split(amount,number):
    return amount / number

main()

#############

# Exercise 3: Unit Converter
def main():
    distance = input("Enter distance in kilometers: ")
    distance = distance.strip()
    if "km" in distance:
        remove_km = distance.lower().replace("km", "").strip()
        print(f"{remove_km} kilometers is equal to {kilometer(remove_km):.3f} miles")
    else:
        convert = kilometer(distance)
        print(f"{distance} kilometers is equal to {convert:.3f} miles")


def kilometer(km):
    float_km = float(km)
    return (float_km * 5) /  3.107


main()

############

# EXERCISE 4: GROCERY LIST

def get_grocery_list():
    grocery_list = []
    while True:
        item = input("Enter an item for the grocery list (or type 'done' to finish): ")
        if item.lower() == "done":
            break
        grocery_list.append(item)
    return grocery_list

def print_grocery_list(grocery_list):
    print("\nYour Grocery List:")
    for i in range(len(grocery_list)):
        print(f"{i + 1}. {grocery_list[i]}")

def main():
    groceries = get_grocery_list()
    print_grocery_list(groceries)

main()
