
import re

text = input("Enter Python source code: ")

comments = re.findall(r'(?m)#.*$', text)
print(comments)
