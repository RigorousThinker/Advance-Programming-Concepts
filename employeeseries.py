import pandas as pd

salary = {
    "Amit": 45000,
    "Riya": 60000,
    "Rahul": 75000,
    "Sneha": 48000,
    "Pooja": 55000
}

s = pd.Series(salary)

print("Employee Salaries:")
print(s)

print("\nHighest Salary:")
print(s.max())

print("\nLowest Salary:")
print(s.min())

print("\nAverage Salary:")
print(s.mean())

print("\nEmployees earning more than 50000:")
print(s[s > 50000])