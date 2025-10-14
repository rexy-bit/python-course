
stop = 1

print("\nWelcom to temp programme")

while stop != 0:
    temp = float(input("Enter a temperature : "))
    if temp > 25:
        print("It's warm")
    elif temp <= 25 and temp > 18:
        print("It's cool")
    else:
        print("It's cold")

        stop = int(input("\nEnter 0 to stop : "))
