
import re

text = input("Enter filenames: ")
print(re.findall(r'\.([A-Za-z0-9]+)\b', text))
