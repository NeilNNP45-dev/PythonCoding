while True:
    operator = input("Enter an operator +,-,*, / or q to quit: ")
    if operator == "q":
        print("All the best and have a nice day")
        break

    Num1 = float(input("Enter Number 1: "))
    Num2 = float(input("Enter Number 2: "))
    if operator == "+":
        result = Num1 + Num2
        print(result)
    elif operator == "-":
        result = Num1 - Num2
        print(result)
    elif operator == "*":
        result = Num1 * Num2
        print(result)
    elif operator == "/":
        result = Num1 / Num2
        print(result)
    else:
        print("Invalid operator. Please enter correct operator.")
