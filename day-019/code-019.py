import sys

#################

# SHORT: TUPLE

def main():
    coordinates = (42.376, -71.115)
    
    latitude,longitude = coordinates

    print(f"Longitude: {coordinates[1]}")
    print(f"Latitude: {coordinates[0]}")

    print(f"Longitude: {longitude}")
    print(f"Latitude: {latitude}")

main()

#######

def main():
    coordinates_tuple = (42.376, -71.115)
    coordinates_list = [42.376, -71.115]
    coordinates_dict = {42.376, -71.115}
    
    print(f"{sys.getsizeof(coordinates_tuple)} bytes")
    print(f"{sys.getsizeof(coordinates_list)} bytes")
    print(f"{sys.getsizeof(coordinates_dict)} bytes")


main()

######################

# SHORT: WHILE LOOPS
"""
def main():
    moisture = sample()
    Days = 0
    print(f"Days: {Days}: Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        days +=1
        print(f"Moisture is {moisture}%")

    print("Time to water")
main()
"""