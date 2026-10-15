
import re

text = input("Enter a sentence: ")
pattern = r'\b(\w+)\s+\1\b'

print(re.findall(pattern, text, re.IGNORECASE))
