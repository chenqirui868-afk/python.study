import pandas as pd


customers = pd.DataFrame({
    "Customer_ID": [1, 2, 3, 4],
    "Name": ["Tom", "Jack", "Lucy", "Mike"]
})

orders = pd.DataFrame({
    "Customer_ID": [1, 2, 3, 5],
    "Product": ["Apple", "Milk", "Juice", "Banana"],
    "Sales": [100, 200, 150, 300]
})
print(pd.merge(customers, orders, on="Customer_ID", how = "inner"))
print(pd.merge(customers, orders, on="Customer_ID", how = "left"))
print(pd.merge(customers, orders, on="Customer_ID", how = "outer"))
print(pd.merge(customers, orders, on="Customer_ID", how ="right"))