import pandas as pd

students = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Asha", "Riya", "Madhuri", "Sneha", "Priya"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "CSE"],
    "Total_Classes": [100, 100, 120, 100, 80],
    "Classes_Attended": [80, 65, 90, 70, 50]
}

df = pd.DataFrame(students)

df["Attendance Percentage"] = (df["Classes_Attended"] / df["Total_Classes"]) * 100

print("Student Attendance:")
print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance Percentage"] < 75])