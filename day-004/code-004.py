## DAY 004 - 18/04/2025
# CS50P: Introduction To Programming with Python**

# LECTURE 1 -CONDITIONALS

###

#IF:
x = int(input("What's x? "))        #Output: What's x? 3
y = int(input("What's y? "))        #Output: What's y? 5

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

##Output: x is less than y

########

# OR:
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

######

