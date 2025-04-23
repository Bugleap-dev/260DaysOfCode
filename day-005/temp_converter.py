#Exercise 2: Temperature Converter

def main():
    temp = input("Enter temperature (Celsius to Fahrenheit and vice-versa): ")      #Receives input from user
    temp = temp.strip().lower()                                                             #Removes leading and trailing whitespaces

    if temp.endswith("c"):                                                 #If the user inputs a degree celsius or C
        celsius_replace = temp.lower().replace("°c", "").replace("c", "" )          #
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