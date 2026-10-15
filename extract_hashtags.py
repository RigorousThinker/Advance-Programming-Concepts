
import re

text = input("Enter a social media post: ")
print(re.findall(r'(?<!\w)#[A-Za-z0-9_]+', text))
