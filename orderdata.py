import pandas as pd

orders = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Amit", "Riya", "Rahul", "Sneha", "Pooja"],
    "Product": ["Laptop", "Mobile", "Keyboard", "Monitor", "Tablet"],
    "Quantity": [1, 2, 5, 2, 3],
    "Price": [50000, 25000, 1500, 12000, 20000],
    "Discount": [2000, 1000, 500, 1000, 1500]
}

df = pd.DataFrame(orders)

df["Final Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final Amount"] > 5000])

print("\nHighest-value order:")
print(df.loc[df["Final Amount"].idxmax()])

print("\nAverage order value:")
print(df["Final Amount"].mean())