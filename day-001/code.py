# print() - creates a new blank line.

print("Hello", "World", "!", sep = "-")
# Output: Hello-World-!

print("Python","is","fun","!",sep=" ")
#Output: Python is fun !

print("Hello",end=" ")
print("World!")
#Output: Hello World!

print("Hello\nWorld")
"""
Output: 
Hello
World
"""

#USING QUOTATION MARK INSIDE PRINT FUNCTION
print('Hello, "friend')
#Output: Hello, "friend

print("Hello, 'friend")
#Output: Hello, 'friend

print('"Hello, "friend"')
#Output: Hello, "friend

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
print(name2.lstrip) #Output:    Dan
print(name2.rstrip) #Output:Dan
print(name2.strip)  #Output:Dan

name3 = "daVid maLan"
first,last = name3.split(" ")
print(name3.capitalize) #Output: David malan
print(name3.title)      #Output: David Malan
print(first)            #Output:daVid