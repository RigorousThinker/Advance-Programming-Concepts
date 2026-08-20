student_marks = {
    "Amit": 75,
    "Riya": 82,
    "Neha": 90,
    "Rahul": 68
}

name = input("Enter student name: ")

if name in student_marks:
    marks = int(input("Enter new marks: "))
    student_marks[name] = marks

print(student_marks)