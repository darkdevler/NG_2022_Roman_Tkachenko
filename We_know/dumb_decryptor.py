enter_message = input("Enter message: ")
enter_step = int(input("Enter step: "))
resultMsg = ""

big_letters =  "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

for i in enter_message:
    big_abc = big_letters.find(i)
    new_big_abc = big_abc + enter_step

    small_abc = small_letters.find(i)
    new_small_abc = small_abc + enter_step

    if i in big_letters:
        resultMsg += big_letters[new_big_abc]
    elif i in small_letters:
        resultMsg += small_letters[new_small_abc]
    else:
        resultMsg += i

print(f"Result: {resultMsg}")