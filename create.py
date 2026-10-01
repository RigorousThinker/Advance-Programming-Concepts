import pandas as pd

students = {
    "Student ID": [101, 102, 103, 104, 105],
    "Student Name": ["Asha", "Riya", "Madhuri", "Sneha", "Priya"],
    "Python Marks": [85, 72, 90, 65, 80],
    "DBMS Marks": [80, 75, 88, 70, 85],
    "Mathematics Marks": [90, 70, 92, 68, 78]
}

df = pd.DataFrame(students)

print("Student Details:")
print(df)

df["Total"] = df["Python Marks"] + df["DBMS Marks"] + df["Mathematics Marks"]

df["Average"] = df["Total"] / 3

print("\nTotal and Average Marks:")
print(df)

print("\nStudents with more than 75% average:")
print(df[df["Average"] > 75])