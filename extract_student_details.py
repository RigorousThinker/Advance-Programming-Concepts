
import re

text = input("Enter student details: ")

pattern = r'Name:\s*([A-Za-z ]+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)'

students = re.findall(pattern, text)

for name, roll, marks in students:
    print(name.strip(), roll, marks)
