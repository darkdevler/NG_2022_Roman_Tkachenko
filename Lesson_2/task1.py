string = input("Enter string: ")
allList = {}
countList = []

for element in range(len(string)):
    if string[element] != " ":
        try:
            allList[string[element].lower()] += 1
        except:
            allList.setdefault(string[element], 1)
        countList.append(string[element])

countList = list(set(countList))

List = ""
for element in range(len(countList)):
    List += f"{countList[element]} - {allList[countList[element]]}; "

countList.sort()
sortingList = ""
for element in range(len(countList)):
    sortingList += f"{countList[element]} - {allList[countList[element]]}; "

print(f"List of all letters: {List}")
print(f"Sorted list of all letters: {sortingList}")