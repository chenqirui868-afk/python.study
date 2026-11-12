import pandas as pd

data = {
    "Product": ["Apple", "Banana", "Milk", "Juice", "Orange"],
    "Category": ["Fruit", "Fruit", "Drink", "Drink", "Fruit"],
    "Sales": [100, 200, 150, 250, 300],
    "Quantity": [10, 20, 15, 25, 30]
}

df = pd.DataFrame(data)
print(df.groupby("Category")["Sales"].sum())
print(df.groupby("Category")["Sales"].mean())
print(df.groupby("Category").size())
print(df.groupby("Category")["Sales"].max())
print(df.groupby("Category")["Sales"].agg(["sum", "mean"]))
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))