file = open("student.txt", "r")

search = input("Enter word to search: ")
total = 0
lines = []

for number, line in enumerate(file, 1):
    words = line.lower().split()

    if search.lower() in words:
        total += words.count(search.lower())
        lines.append(number)

print("Number of occurrences:", total)
print("Line numbers:", lines)

file.close()