enter_list = input("Enter list: ").replace(" ", "")
listStr = list(set(enter_list.split(",")))
print(f"Your sorted list: {listStr}")