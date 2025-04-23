# Exercise 3: Tip Calculator

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