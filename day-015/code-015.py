
#SHORT : DICTOINARIES

def main():
    spacecraft = { "name": "Voyager 1", "distance":163}
    report = create_report(spacecraft["name"],spacecraft["distance"])
    print(report)

def create_report(name,distance):
    return f"""
    ============= REPORT ==============

    Name: {name}
    Distance: {distance} AU

    ===================================

    """

main()

########################

def main():
    spacecraft = { "name": "Voyager 1", "distance":163}
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ============= REPORT ==============

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU

    ===================================

    """

main()

#########################

def main():
    spacecraft = { "name": "James Webb Space Telescsope"}
    spacecraft["distance"] = 0.01
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ============= REPORT ==============

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU

    ===================================
    """

main()

#########################

spacecraft = {
    "name": "James Webb Space Telescsope"
    }
spacecraft["distance"] = 0.01
print(spacecraft.get("owner","Unknown"))                # .get(str,str) => is used to get the value of a key-value
print(spacecraft)                                       # pair in a dictionary by stating the key, and it returns a default value if stated

########################

spacecraft = {
    "name": "Voyager 1",
    "distance" : "12",
    "owner": "Benjamin"
}
spacecraft.update({
    "company":"Umbrella corp.",
    "location":"Milky way"
    })

print(spacecraft["location"])

#########################

distances = {
    "Voyager 1": 163,
    "Voyager 2": 135,
    "Pioneer 10": 80,
    "Pioneer 11": 44,
    "New Horizon": 58
}

def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth.")


main()
#########################

distances = {
    "Voyager 1": 163,
    "Voyager 2": 135,
    "Pioneer 10": 80,
    "Pioneer 11": 44,
    "New Horizon": 58
}

def main():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance):,}m")

def convert(au):
    return au * 149597870700
main()

