number = int(input("Enter number: "))
factorial = 1

while number > 1:
    factorial *= number
    number -= 1

print(f"Result: {factorial}")