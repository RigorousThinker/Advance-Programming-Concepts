
import re

text = input("Enter a sentence: ")
print(re.findall(r'\b\w+s\b', text, re.IGNORECASE))
