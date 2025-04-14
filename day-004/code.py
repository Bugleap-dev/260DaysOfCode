## DAY 004 - 13/04/2025
# 


def greet(input):
    if "hello" in input:
        return "hello there!"
    else:
        return "I'm not sure what you mean"

greeting = greet("hello, computer")
print(greeting)
#Output 
# hello there


#
x = int(input("What's x?: "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

#

def main():
    x = int(input("What's x?: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")        


def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False
    
main()

#
def main():
    x = int(input("What's x?: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")        


def is_even(n):
    return True if n % 2 == 0 else False

main()

#
def main():
    x = int(input("What's x?: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")        


def is_even(n):
    return n % 2 == 0

main()

#
name = input("What's your name: ")
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Griffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

##
name = input("What's your name: ")
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

##
##
name = input("What's your name: ")
match name:
    case "Harry"|"Hermione"|"Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
