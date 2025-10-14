import math

"""
x = 2
rate = 4.09
my_name = "Yanis"
print(my_name)
print("My rate is : ", rate)
print(len(my_name))
print(my_name[0])
print(my_name[-1])
print(my_name[0:3])
course = "python \" programming language"
print(course)
print(len(course))
first = "yanis"
last = "rezgui"
full = first + " " + last
print(full)
"""
""""
course = "   python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.replace("p", "j"))
"""

# Numbers
"""
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
"""
# Loops

# For Loop
"""
for i in range(5):
    for j in range(4):
        print(f"[{i},{j}]")


print(type(5))
"""

# while Loop

command = ""

while command != "quit" and command != "QUIT":
    command = input(">")
    print("ECHO", command)
