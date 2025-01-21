# A comment just in case of any emergency

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

# Menu options
print("Choose an operation:")
print("[ 1 ] ADD")
print("[ 2 ] SUBTRACT")
print("[ 3 ] MULTIPLY")
print("[ 4 ] DIVIDE")

# Get user input
choice = input(">> ")

# Get two numbers from user
try:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    
    # Perform operation based on choice
    if choice == "1":
        print(f"The result is: {add(num1, num2)}")
    elif choice == "2":
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == "3":
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == "4":
        print(f"The result is: {divide(num1, num2)}")
    else:
        print("ERROR: Choose an option between 1 and 4.")
except ValueError:
    print("Invalid input! Please enter valid numbers.")
