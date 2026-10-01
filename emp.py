import pandas as pd

employees = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Employee Name": ["Amit", "Riya", "Rahul", "Sneha", "Pooja"],
    "Department": ["IT", "HR", "Sales", "IT", "Finance"],
    "Salary": [55000, 45000, 60000, 48000, 70000],
    "Experience": [3, 2, 5, 4, 7]
}

df = pd.DataFrame(employees)

print("Employee Details:")
print(df)

print("\nEmployees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nEmployee with highest experience:")
print(df.loc[df["Experience"].idxmax()])