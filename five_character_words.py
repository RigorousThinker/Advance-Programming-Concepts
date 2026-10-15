
import re

text = input("Enter a sentence: ")
print(re.findall(r'\b[A-Za-z]{5}\b', text))
