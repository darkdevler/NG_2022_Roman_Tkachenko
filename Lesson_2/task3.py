enter_number = int(input("Enter number: "))
number = enter_number

if enter_number <= 0:
    print("Your number is less than or equal to 0!")

while enter_number > 0:
    result = ""

    while number > 0:
        result += f"{number} "
        number -= 1

    enter_number -= 1
    number = enter_number

    print(result)