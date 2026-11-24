from pathlib import Path

import pandas as pd

# Resolve paths relative to this script so the file works from any working directory.
base_dir = Path(__file__).resolve().parent
orders = pd.read_csv(base_dir / "data" / "orders.csv")
customers = pd.read_csv(base_dir / "data" / "customers.csv")

print("Orders Shape:")
print(orders.shape)

print("Customers Shape:")
print(customers.shape)

print("Orders Info:")
print(orders.info())

print("Customers Info:")
print(customers.info())

print("Orders Status:")
print(orders["Status"].value_counts())

print("Duplicate Order IDs:")
print(orders.duplicated(subset=["Order_ID"]).sum())

orders["Order_Date"] = pd.to_datetime(orders["Order_Date"], errors="coerce")
print(orders["Order_Date"].dtype)

# Filter completed transactions and remove duplicate order IDs.
completed_orders = orders.loc[
    orders["Status"] == "Completed"
].copy()


# Clean fields used for RFM analysis.
completed_orders["Quantity"] = pd.to_numeric(
    completed_orders["Quantity"], errors="coerce"
)
completed_orders["Unit_Price"] = pd.to_numeric(
    completed_orders["Unit_Price"], errors="coerce"
)
completed_orders = completed_orders.dropna(
    subset=["Customer_ID", "Order_Date", "Quantity", "Unit_Price"]
)
completed_orders["Sales"] = (
    completed_orders["Quantity"] * completed_orders["Unit_Price"]
)

print("\nCompleted Orders:")
print(completed_orders.shape)
print(completed_orders.head())

print("\nMost Recent Completed Order Per Customer:")
print(completed_orders.groupby("Customer_ID", as_index=False)["Order_Date"].max())

last_purchase = completed_orders.groupby("Customer_ID")["Order_Date"].max()
reference_date = pd.to_datetime("2025-06-13")
recency = (reference_date - last_purchase).dt.days
print(recency)
frequency = completed_orders.groupby("Customer_ID")["Order_ID"].nunique()
print(frequency)
monetary = completed_orders.groupby("Customer_ID")["Sales"].sum()
print(monetary)
rfm = pd.concat([recency, frequency, monetary], axis=1)
rfm.columns = ["Recency", "Frequency", "Monetary"]
rfm = rfm.reset_index().rename(columns={"index": "Customer_ID"})
print("===== NEW RFM OUTPUT =====")
print(rfm)
print(rfm.columns)