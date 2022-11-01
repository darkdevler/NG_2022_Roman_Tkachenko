def enter_first_number():
    first_number = int(input("Enter the first number: "))
    return first_number

def enter_second_number():
    second_number = int(input("Enter the second number: "))
    return second_number

def input_operation():
    operation = input("Input operation: «+, -, *, /, ^, sqrt»: ")
    return operation

def addNumbers(first_number, second_number):
    result = first_number + second_number
    return result

def minusNumbers(first_number, second_number):
    result = first_number - second_number
    return result

def multiplyNumbers(first_number, second_number):
    result = first_number * second_number
    return result

def divideNumbers(first_number, second_number):
    result = first_number / second_number
    return result

def sqNumbers(first_number, second_number):
    result = first_number ** second_number
    return result

def sqrtNumbers(first_number, second_number):
    select_number = input("Choose from which number you want to get the root (1 or 2): ")
    if select_number == "1":
        result = first_number ** (0.5)
    if select_number == "2":
        result = second_number ** (0.5)
    return result

def started():
    first_number = enter_first_number()
    second_number = enter_second_number()
    operation = input_operation()

    if operation == "+":
        result = addNumbers(first_number, second_number)

    elif operation == "-":
        result = minusNumbers(first_number, second_number)

    elif operation == "*":
        result = multiplyNumbers(first_number, second_number)

    elif operation == "/":
        result = divideNumbers(first_number, second_number)

    elif operation == "^":
        result = sqNumbers(first_number, second_number)

    elif operation == "sqrt":
        result = sqrtNumbers(first_number, second_number)

    else:
        result = "Error! There is no such operation."

    print(f"Result: {result}")

started()