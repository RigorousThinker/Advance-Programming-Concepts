
import re

text = input("Enter text: ")
text = re.sub(r'<.*?>', '', text)
text = re.sub(r'\s+', ' ', text)
text = re.sub(r'[^\w\s.,!?]', '', text)
print(text.strip())
