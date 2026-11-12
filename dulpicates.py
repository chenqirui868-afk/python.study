import pandas as pd

data = {
    "Order_ID": [101, 102, 103, 103, 104, 105, 105],
    "Product": ["Apple", "Banana", "Milk", "Milk", "Juice", "Orange", "Orange"],
    "Sales": [100, 200, 150, 150, 250, 300, 300]
}

df = pd.DataFrame(data)

print(df)
print(df.duplicated())
print(df.duplicated().sum())
print(df.drop_duplicates())
print(df.drop_duplicates(subset=["Order_ID"]))