AIM
To write a Python program to implement a simple calculator using control flow and looping statements.

ALGORITHM
1.Start.
2.Display the calculator menu.
3.Read the user's choice.
4.Enter two numbers.
5.Use if-elif-else to perform the selected operation.
6.Display the result.
7.Repeat the process using a while loop.
8.If the user chooses Exit, stop the loop.
9.Stop.# Calculator using control flow and looping statements


CODE
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

OUTPUT
--- CALCULATOR ---
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter your choice: 1
Enter first number: 10
Enter second number: 5
Result = 15.0

Enter your choice: 3
Enter first number: 10
Enter second number: 5
Result = 50.0

Enter your choice: 5
Calculator closed.
