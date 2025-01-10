def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def devide(num1, num2):
    return num1 / num2

print("Choose an operation. ")
print("Type a number ")
print("[ 1 ] ADD")
print("[ 2 ] SUBTRACT")
print("[ 3 ] MULTIPLY")
print("[ 4 ] DEVIDE")
choice = input(">> ")
if type(choice) != number:
    print("Not a number, please type a number") 