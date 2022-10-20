first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

operation = input("Input operation: «+, -, *, /, ^, sqrt»: ")

if operation == "+":
    result = first_number + second_number

if operation == "-":
    result = first_number - second_number

if operation == "*":
    result = first_number * second_number

if operation == "/":
    result = first_number / second_number

if operation == "^":
    result = first_number ** second_number

if operation == "sqrt":
    select_number = input("Choose from which number you want to get the root (1 or 2): ")
    if select_number == "1":
        result = first_number ** (0.5)
    if select_number == "2":
        result = second_number ** (0.5)

else:
    result = "Error! There is no such operation."

print(f"Result: {result}")