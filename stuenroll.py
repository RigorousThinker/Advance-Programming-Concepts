python_students = {"Amit", "Rahul", "Sneha", "Priya", "Neha"}
java_students = {"Sneha", "Priya", "Rohit", "Karan", "Neha"}

both_courses = python_students.intersection(java_students)
only_one_course = python_students.symmetric_difference(java_students)

print("Students enrolled in both courses:", both_courses)
print("Students enrolled in only one course:", only_one_course)
