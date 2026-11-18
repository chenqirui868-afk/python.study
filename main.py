from pathlib import Path

import pandas as pd

base_dir = Path(__file__).resolve().parent
customer = pd.read_csv(base_dir / "customers.csv")
orders = pd.read_csv(base_dir / "orders.csv")

print("Customers Shape:", customer.shape)
print("Orders Shape:", orders.shape)

print(customer.info())
print(orders.info())

print("Customers Missing:")
print(customer.isnull().sum())
print("Orders Missing:")
print(orders.isnull().sum())

print("Customers Duplicates:")
print(customer.duplicated().sum())
print("Orders Duplicated:")
print(orders.duplicated().sum())

print("Customers Duplicate Rows:")
print(customer.duplicated(keep=False))
print("Orders Duplicate Rows:")
print(orders.duplicated(keep=False))

print("Orders Missing Rows:")
print(orders[orders.isnull().any(axis=1)])

print("Customers Duplicate:")
print(customer[customer.duplicated(keep=False)])
print("Orders Duplicate:")
print(orders[orders.duplicated(keep=False)])

customer = customer.drop_duplicates()
orders = orders.drop_duplicates()

print("Customers Duplicates After Cleaning:")
print(customer.duplicated().sum())
print("Orders Duplicated After Cleaning:")
print(orders.duplicated().sum())

print("Missing Unit_Price:")
print(orders[orders["Unit_Price"].isna()])

print("Missing Customer_ID:")
print(orders[orders["Customer_ID"].isna()])

keyboard_orders = orders[
    orders["Product"] == "Keyboard"
]

print(keyboard_orders)

print(orders.groupby("Product")["Unit_Price"].agg(
    ["count", "min", "max", "mean", "median"]
))