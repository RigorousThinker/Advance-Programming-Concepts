file = open("student.txt", "r")
text = file.read()
file.close()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

text = text.replace(old_word, new_word)

file = open("newstudent.txt", "w")
file.write(text)
file.close()

print("File updated successfully.")