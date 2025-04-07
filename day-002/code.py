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
m = int(input("what's m?: "))  #what's m?: 3
n = int(input("What's n?: "))  #what's n?: 4
print(m+n)                     #7

#FLOAT:
x = float(input("what's x?: "))  #what's x?: 4.5
y = float(input("What's y?: "))  #what's y?: 4.4
print(x+y)                       #8.9

#ROUND() FUNCTION:
a = float(input("what's a?: "))  #what's a?: 999
b = float(input("What's b?: "))  #what's b?: 1
c = round(a+b)
print(f"{c:,}")
#Output: 1,000

round(4.6)      #Output: 5
round(4.3)      #Output: 4
round(5.5)      #Output: 6 (to the nearest whole number)

round(3.14159,2)      #Output: 3.14
round(2.71828,3)      #Output: 2.718

round(-2.5)      #Output: -2    | ROUND HALF TO EVEN OR
round(-3.5)      #Output: -4    | BANKER'S ROUNDING

j = float(input("what's j?: "))  #what's j?: 253
k = float(input("What's k?: "))  #what's k?: 13
l = j/k

print(f"{l:.1f}")        #Output: 19.5
print(f"{l:.2f}")       #Output: 19.46
print(f"{l:.3f}")       #Output: 19.462


#def FUNCTION:
#1
def hello(to= "World" ):                #Deines a function named hello, with one parameter (to),and a default parameter value of "World"
    print("hello", to)                  #i.e if no argument is passed when calling hello(), it will use "World as the default"


hello()                                 #this calls the function. Output: hello World
name4 = input ("What's your name?: ")   #Output: What's your name?: Dan
hello(name4)                            #Output: hello Dan


#2
def main():                                 #Define the main function
    name5 = input("What's your name?: ")    #Ask the user for their name
    hello(name5)                            #call the hello function with the user's name
                                            
                                            
def hello(to="World"):                      #Define the hello function with a defaiult parameter
    print("hello,",to)                      #prints a greeting
                                            
main()                                      #call the main function to start the program

#return
def add (a,b):
    return a+b

result1 = add(3,4)
print(result1)       #Output: 7

#
def main():                             #Define a function called main
    v = float(input("What's v? "))      #convert the user input into a float
    print("v squared is", square(v))

def square(n):                          #Define a function called square
    return n**2                         #Returns the square of the value n

main()                                  #Calls the function main

