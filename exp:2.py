# Calculator using control flow and looping statements

while True:
    print("\n--- CALCULATOR ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Calculator closed.")
        break

    if choice < 1 or choice > 5:
        print("Invalid choice!")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = num1 + num2
        print("Result =", result)

    elif choice == 2:
        result = num1 - num2
        print("Result =", result)

    elif choice == 3:
        result = num1 * num2
        print("Result =", result)

    elif choice == 4:
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            result = num1 / num2
            print("Result =", result)
