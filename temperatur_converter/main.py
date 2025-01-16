def getTemp():
    while True:
        temp = input("Enter the temp: ").strip()
        
        try:
            temp = float(temp)
            return temp
        except ValueError:
            print("Enter a valid temperature.")
            continue

temp = getTemp()

print("[ 1 ] Convert to C.")
print("[ 2 ] Convert to F.")

while True:
    choice = input("Choose one: ").strip()
    
    if choice == "1":
        converted = round((temp - 32) * 5/9, 2)
        print(f"It's {converted} Celsius.")
        break
    elif choice == "2":
        converted = round(temp * 9/5 + 32, 2)
        print(f"It's {converted} Fahrenheit.")
        break
    else:
        print("Invalid choice, try again.")
        continue
