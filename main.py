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
orders["Quantity"] = orders["Quantity"].replace("two", 2)
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
print(completed_orders.loc[
    completed_orders["Order_ID"] == "O1014",
    ["Order_ID", "Quantity", "Unit_Price"]
])
completed_orders["Sales"] = (
    completed_orders["Quantity"] * completed_orders["Unit_Price"]
)

print("\nCompleted Orders:")
print(completed_orders.shape)
print(completed_orders.head())

print("\nMost Recent Completed Order Per Customer:")
print(completed_orders.groupby("Customer_ID", as_index=False)["Order_Date"].max())

last_purchase = completed_orders.groupby("Customer_ID")["Order_Date"].max()
reference_date = pd.to_datetime("2025-06-15")
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
missing_customers = customers.loc[
    ~customers["Customer_ID"].isin(rfm["Customer_ID"]),
    "Customer_ID"
]
print(missing_customers)
print(orders[orders["Customer_ID"].isin(["C005","C006"])])
print(completed_orders[completed_orders["Customer_ID"].isin(["C005","C006"])])
print(completed_orders["Customer_ID"].unique())
# Check the original order O1014
print("\n===== CHECK ORDER O1014 =====")

print(
    orders.loc[
        orders["Order_ID"] == "O1014"
    ]
)
print(
    orders.loc[
        orders["Order_ID"] == "O1014",
        ["Order_ID", "Customer_ID", "Quantity", "Unit_Price", "Status"]
    ].to_string(index=False)
)
print(orders.loc[orders["Order_ID"] == "01014"])
rfm["M_Score"] = pd.qcut(
    rfm["Monetary"],
    5,
    labels=[1, 2, 3, 4, 5]
)
rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    5,
    labels=[5, 4, 3, 2, 1]
)
print(rfm[["Customer_ID", "Monetary", "M_Score", "Recency", "R_Score"]])