s = input("Enter a string: ")

char = input("Enter character to find frequency: ")

count = 0

for ch in s:
    if ch == char:
        count += 1

print("Frequency:", count)