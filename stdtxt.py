name = input("Enter student name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")
file.write("Branch: " + branch + "\n")
file.write("Semester: " + semester + "\n")

file.close()

print("Student information saved successfully.")