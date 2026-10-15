
import re

text = input("Enter text: ")
print(re.findall(r'[ \t\n]', text))
