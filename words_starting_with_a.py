
import re

text = input("Enter a sentence: ")
print(re.findall(r'\b[Aa]\w*\b', text))
