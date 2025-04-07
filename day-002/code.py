# CONTINUATION OF LECTURE 0: FUNCTION_VARIRABLE

name1 = input("What's your name: ")
print(f"hello, {name1}")
"""
Output: What's your name: Dan
hello, Dan
"""

print(len("hello"))
#Output: 5

print (str(123))
#Output: 123

print(type("hello"))
#Output: str

name2= "    Dan " 
print(name2.lstrip()) #Output:    Dan
print(name2.rstrip()) #Output:Dan
print(name2.strip())  #Output:Dan

name3 = "daVid maLan"
first,last = name3.split(" ")
print(name3.capitalize()) #Output: David malan
print(name3.title())      #Output: David Malan
print(first)            #Output:daVid

#INTGERS:
x = int(input("what's x?: "))  #what's x?: 3
y = int(input("What's y?: "))  #what's y?: 4
print(x+y)                     #7

#FLOAT:
x = float(input("what's x?: "))  #what's x?: 4.5
y = float(input("What's y?: "))  #what's y?: 4.4
print(x+y)                       #8.9

#ROUND() FUNCTION:
x = float(input("what's x?: "))  #what's x?: 999
y = float(input("What's y?: "))  #what's y?: 1
z = round(x+y)
print(f"{z:,}")
#Output: 1,000

round(4.6)      #Output: 5
round(4.3)      #Output: 4
round(5.5)      #Output: 6 (to the nearest whole number)

round(3.14159,2)      #Output: 3.14
round(2.71828,3)      #Output: 2.718

round(-2.5)      #Output: -2    | ROUND HALF TO EVEN OR
round(-3.5)      #Output: -4    | BANKER'S ROUNDING

x = float(input("what's x?: "))  #what's x?: 253
y = float(input("What's y?: "))  #what's y?: 13
z = x/y

print(f"{z:.f}")        #Output: 19.5
print(f"{z:.2f}")       #Output: 19.46
print(f"{z:.3f}")       #Output: 19.462

#def FUNCTION:
def hello(to):
    print("hello", to)


name = input ("What's your name?: ")
hello(name)

def greet(name):
    return f"Hello, {to}!"


name = "dan"
greet(name)