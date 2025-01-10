from random import randint

# Generate a random number between 1 and 20
number = randint(1, 20)

print("Guess a number between 1-20.")

while True:
    # Input from the user
    guess = input(">> ")
    
    # Check if the user input is a valid integer
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)

    # Compare the guess with the random number
    if guess == number:
        print("YESSS! You got it.")
        break
    else:
        print("NO, try again!")
