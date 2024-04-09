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

        """ 0으로 나눌 수 없음 -> ZeroDivisionError
        result = num1 / num2
        print("The result is ", result)
        """
        
        try:
            result = num1 / num2
            print("The result is ", result)
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")

    else:
        print("Invalid operation. Please choose from +, -, *, /.")

calculator()