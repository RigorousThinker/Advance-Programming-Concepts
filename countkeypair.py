employees = {
    101: "Amit",
    102: "Riya",
    103: "Neha",
    104: "Rahul"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")