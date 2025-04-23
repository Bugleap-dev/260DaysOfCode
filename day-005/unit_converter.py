# Exercise 1: Unit Converter
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