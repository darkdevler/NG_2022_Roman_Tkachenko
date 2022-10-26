a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

solution_discriminant = b ** 2 - 4 * a * c

if solution_discriminant > 0:
    result = f"Result: x1 = {(-b + solution_discriminant ** 0.5) / (a * 2)}, x2 = {(-b - solution_discriminant ** 0.5) / (a * 2)}"

elif solution_discriminant == 0:
    result = f"Result: x = {-b / (a * 2)}"

elif solution_discriminant < 0:
    result = "There are no roots :D"

else:
    result = "Something is wrong here..."

print(result)