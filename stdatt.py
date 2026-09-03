file = open("attendance.txt", "r")

for line in file:
    roll, name, present, total = line.strip().split(",")

    percentage = (int(present) / int(total)) * 100

    print(name, "Attendance:", percentage, "%")

    if percentage < 75:
        print("Below 75%:", name)

file.close()