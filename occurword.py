file = open("student.txt", "r")
text = file.read().lower()

words = text.split()
count = {}

for word in words:
    word = word.strip(".,!?;:")
    count[word] = count.get(word, 0) + 1

print(count)

file.close()