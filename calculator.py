def calculator():
    # Prompt the user to input the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt the user to input the second number
    num2 = float(input("Enter the second number: "))
    
    # Prompt the user to choose an arithmetic operation
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the number corresponding to the operation: ")
    
    # Perform the calculation based on the user's choice
    if operation == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == '3':
        result = num2 * num1
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice.")

# Call the calculator function
calculator()