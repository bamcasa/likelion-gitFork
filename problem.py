# 이 프로그램에는 문제가 있어요. 문제를 찾아서 수정해주세요.

def calculator():
    operation = input("Choose the operation (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        result = num1 + num2
        print("The result is ", result)

    elif operation == '-':
        result = num1 - num2
        print("The result is ", result)

    elif operation == '*':
        result = num1 * num2
        print("The result is ", result)

    elif operation == '/':
        result = num1 / num2
        print("The result is ", result)

    else:
        print("Invalid operation. Please choose from +, -, *, /.")

calculator()