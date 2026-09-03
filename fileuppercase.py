file = open("student.txt", "r")
text = file.read()
file.close()

new_file = open("uppercase.txt", "w")
new_file.write(text.upper())
new_file.close()

print("Uppercase file created successfully.")