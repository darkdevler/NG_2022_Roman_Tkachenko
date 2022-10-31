enter_list = input("Enter list: ")
numbers_list = list(map(int, enter_list.split(",")))
numbers_list.sort()

small_number = numbers_list[0]
largest_number = numbers_list[-1]
all_numbers = sum(numbers_list[1:-1])

print(f"Smallest number: {small_number};\nLargest number: {largest_number};\nSum all numbers: {all_numbers};")