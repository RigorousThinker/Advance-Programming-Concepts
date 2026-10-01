import pandas as pd

marks = {
    "Asha": 85,
    "Riya": 72,
    "Madhuri": 90,
    "Sneha": 68,
    "Priya": 80
}

s = pd.Series(marks)

print("Student Marks:")
print(s)

print("\nMarks of Madhuri:")
print(s["Madhuri"])

print("\nMaximum Marks:")
print(s.max())

print("\nMinimum Marks:")
print(s.min())

print("\nAverage Marks:")
print(s.mean())

print("\nStudents scoring more than 75:")
print(s[s > 75])
