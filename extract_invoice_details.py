
import re

text = input("Enter invoice text: ")

invoice = re.findall(r'Invoice\s*(?:No\.?|Number|#)\s*:?\s*([A-Z0-9/-]+)', text, re.IGNORECASE)
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
amounts = re.findall(r'(?:₹|Rs\.?|INR)\s*[\d,]+(?:\.\d{2})?', text, re.IGNORECASE)

print("Invoice numbers:", invoice)
print("Dates:", dates)
print("Amounts:", amounts)
