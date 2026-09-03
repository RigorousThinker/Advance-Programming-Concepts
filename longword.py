file = open("student.txt", "r")
text = file.read()

words = text.split()
words = [word.strip(".,!?;:") for word in words]

longest = max(words, key=len)

print("Longest word:", longest)

file.close()