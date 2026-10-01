import pandas as pd

prices = {
    "Laptop": 50000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Headphones": 2500,
    "Pen Drive": 700
}

s = pd.Series(prices)

print("Products and Prices:")
print(s)

s = s * 1.10

print("\nPrices after 10% increase:")
print(s)

print("\nMost Expensive Product:")
print(s.idxmax(), s.max())

print("\nProducts costing more than 1000:")
print(s[s > 1000])