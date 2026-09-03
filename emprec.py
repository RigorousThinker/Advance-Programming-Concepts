def read_employees():
    file = open("employees.txt", "r")
    employees = []

    for line in file:
        emp_id, name, department, salary = line.strip().split(",")
        employees.append((emp_id, name, department, float(salary)))

    file.close()
    return employees


def display_employees(employees):
    print("All Employees:")
    for employee in employees:
        print(employee)


def highest_paid(employees):
    employee = max(employees, key=lambda x: x[3])
    print("Highest-paid employee:", employee[1])
    print("Salary:", employee[3])


def average_salary(employees):
    average = sum(employee[3] for employee in employees) / len(employees)
    print("Average salary:", average)


def above_salary(employees):
    salary = float(input("Enter salary: "))

    print("Employees earning above", salary, ":")
    for employee in employees:
        if employee[3] > salary:
            print(employee)


employees = read_employees()

display_employees(employees)
highest_paid(employees)
average_salary(employees)
above_salary(employees)