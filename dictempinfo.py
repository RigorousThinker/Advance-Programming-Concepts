employee = {
    "name": "Rahul",
    "age": 25,
    "department": "IT",
    "salary": 40000
}

key = input("Enter key: ")

if key in employee:
    print(employee[key])
else:
    print("Key not found")
    