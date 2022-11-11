separator = "--- --- >>> * <<< --- ---"

def enter_string():
    string = input("Enter string: ")
    return string

def select_action():
    action = input(f"{separator}\n"
                   "Available actions:\n"
                   "1. Sort string\n"
                   "2. Count the number of elements\n"
                   "3. Display vowels or consonants letters\n"
                   "4. Split by words, and output words from the end\n"
                   "5. Print word by number\n"
                   "6. Enter line again\n"
                   "7. Exit\n"
                   f"{separator}\n"
                   "Select action: ")
    return action

def sorted_string(string: str):
    our_string = string.split(" ")
    our_string.sort()
    return " ".join(our_string)

def elements_count(string: str):
    our_string = len(string.split(" "))
    return our_string

def enter_letters():
    enter_letters = input(f"{separator}\nSelect an action:\na) Display vowels letters\nb) Display consonants letters\n")
    return enter_letters

def displayLettersType(string: str, enter_letters: str):
    vowels_list = "аоиыеэуюяіїєaeiouy"

    result_string = ""
    for letter in string:
        if letter == " ":
            result_string += letter
            continue

        if enter_letters == "a":
            if letter.lower() in vowels_list:
                result_string += letter

        elif enter_letters == "b":
            if letter.lower() not in vowels_list:
                result_string += letter

        else:
            result_string = "Unknown action!"
    return result_string

def reverse_words(string: str):
    result_string = string.split(" ")
    result_string.reverse()
    return (" ".join(result_string))

def word_by_number(string: str):
    our_string = string.split(" ")
    enter_number = int(input(f"{separator}\nEnter word number:\n"))
    result = f"Word with number {enter_number} in the list: {our_string[enter_number - 1]}"
    return result

def processing_action():
    string = enter_string()
    action = select_action()

    match action:
        case "1":
            result = sorted_string(string)
            print(f"{separator}\nResult: {result}\n{separator}\n")
        case "2":
            result = elements_count(string)
            print(f"{separator}\nResult: {result}\n{separator}\n")
        case "3":
            result = displayLettersType(string, enter_letters())
            print(f"{separator}\nResult: {result}\n{separator}\n")
        case "4":
            result = reverse_words(string)
            print(f"{separator}\nResult: {result}\n{separator}\n")
        case "5":
            result = word_by_number(string)
            print(f"{separator}\nResult: {result}\n{separator}\n")
        case "6":
            print(f"{separator}\nOkay! You can enter string again.")
            return processing_action()
        case "7":
            print(f"{separator}\nOkay! The program is closed.\n{separator}\n")

processing_action()