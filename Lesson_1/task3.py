seconds_number = int(input("Enter number of seconds: "))

day = int(seconds_number / 86400)
hours = int((seconds_number % 86400) / 3600)
minutes = int(((seconds_number % 86400) % 3600) / 60)
seconds = int(((seconds_number % 86400) % 3600) % 60)

result = f"Day: {day} Time: {hours}:{minutes}:{seconds}"
print(result)