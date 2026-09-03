file = open("students.txt", "r")

students = []

next(file)

for line in file:
    roll, name, marks = line.strip().split(",")
    students.append((roll, name, int(marks)))

file.close()

print("All Records:")
for student in students:
    print(student)

highest = max(students, key=lambda x: x[2])
average = sum(student[2] for student in students) / len(students)

print("Highest Marks:", highest[1], highest[2])
print("Average Marks:", average)

print("Students scoring more than 80:")
for student in students:
    if student[2] > 80:
        print(student[1], student[2])