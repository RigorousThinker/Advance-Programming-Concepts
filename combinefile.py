file1 = open("file1.txt", "r")
text1 = file1.read()
file1.close()

file2 = open("file2.txt", "r")
text2 = file2.read()
file2.close()

file3 = open("combined.txt", "w")
file3.write(text1)
file3.write("\n")
file3.write(text2)
file3.close()

print("Files combined successfully.")