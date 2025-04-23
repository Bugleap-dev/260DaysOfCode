

#####

students = ["Hermione", "Ron","Harry"]

for student in students:
    print(student)

#####

students = ["Hermione", "Ron","Harry"]

for i in range(len(students)):
    print(i+1, students[i])

#####

#dict:

students = {
    "Hermione": "Griffindor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin"
}

print(students["Ron"])          #Output: "Griffindor"

for student in students:
    print(student)

"""
Output:
Hermione
Harry
Ron
Draco
"""

for student in students:
    print(student, students[student],sep = ", ")

"""
Output:
Hermione, Griffindor
Harry, Griffindor
Ron, Griffindor
Draco, Slytherin
"""

#####
#USING DICTIONARY IN LIST
students = [

    {"name": "Hermione", "house":"Griffindor", "patronus": "Otter"},
    {"name":"Harry", "house":"Griffindor", "patronus": "Stag"},
    {"name":"Ron", "house":"Griffindor","patronus": "Jack Russell terrier"},
    {"name":"Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"],sep = ", ")

"""
Output:
Hermione, Griffindor, Otter
Harry, Griffindor, Stag
Ron, Griffindor, Jack Russell terrier
Draco, Slytherin, None
"""

#####

#Mario:

def main():
    print_column(3)

def print_column(height):
    print("#\n" * height,end="")

main()

#####

def main():
    print_square(4)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
            
        print()    


main()