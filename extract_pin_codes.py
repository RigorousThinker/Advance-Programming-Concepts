
import re

text = input("Enter a paragraph: ")
print(re.findall(r'(?<!\d)[1-9]\d{5}(?!\d)', text))
