file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

if lines1 == lines2:
    print("Both files are identical.")
else:
    print("Files are different.")

    limit = min(len(lines1), len(lines2))

    for i in range(limit):
        if lines1[i] != lines2[i]:
            print("First difference is at line:", i + 1)
            print("File 1:", lines1[i].strip())
            print("File 2:", lines2[i].strip())
            break

    if len(lines1) != len(lines2) and lines1[:limit] == lines2[:limit]:
        print("Files have different number of lines.")