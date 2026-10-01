import pandas as pd

products = {
    "Product ID": [101, 102, 103, 104, 105],
    "Product Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
    "Price": [50000, 800, 1500, 12000, 2500],
    "Quantity": [2, 10, 5, 3, 8]
}

df = pd.DataFrame(products)

df["Total Amount"] = df["Price"] * df["Quantity"]

print(df)

print("\nProduct with highest total sales:")
print(df.loc[df["Total Amount"].idxmax()])