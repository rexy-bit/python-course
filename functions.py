
def increment(number, by):
    return number + by


result = increment(2, 1)
print(result)

number = 0


def increment2(*numbers):
    total = 1
    for i in numbers:
        total *= i

    return total


total = increment2(1, 2, 3)
print(total)
