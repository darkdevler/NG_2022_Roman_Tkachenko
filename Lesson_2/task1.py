string = input("Enter string: ")
allList = {}
countList = []

for i in range(len(string)):
    if string[i] != " ":
        try:
            allList[string[i].lower()] += 1
        except:
            allList.setdefault(string[i].lower(), 1)
        countList.append(string[i].lower())

countList = list(set(countList))

List = ""
for i in range(len(countList)):
    List += f"{countList[i]} - {allList[countList[i]]}; "

countList.sort()
sortingList = ""
for i in range(len(countList)):
    sortingList += f"{countList[i]} - {allList[countList[i]]}; "

print(f"List of all letters: {List}")
print(f"Sorted list of all letters: {sortingList}")