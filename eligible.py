
"""
age = int(input("\nEnter Your Age : "))

message = "Eligible" if age >= 18 else "Not Eligible"

print(message)


age = int(input("\nEnter the age of the employee : "))

if 18 <= age < 65:
    print("You ca still work")
elif age < 18:
    print("\nYou are still young you are not allowed to work")
elif age >= 60:
    print("You can retire")

    """

# Disp Even between 1 to 10

cpt = 0
print("Even Numbers between 1 to 10 are : ")
for number in range(1, 11):
    if number % 2 == 0:
        print(number)
        cpt += 1

print("We have ", cpt, "Even Numbers")
