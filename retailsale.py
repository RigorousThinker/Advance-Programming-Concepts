import pandas as pd

products = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Tablet"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 25000, 1500, 12000, 20000],
    "Quantity": [2, 3, 10, 2, 1]
}

df = pd.DataFrame(products)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("Product Data:")
print(df)

print("\nProducts with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nAverage Sales:")
print(df["Total_Sales"].mean())