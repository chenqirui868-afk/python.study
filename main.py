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
rfm["F_Score"] = rfm["Frequency"].map({1:1,2:5})
print(rfm[["Customer_ID","Frequency","F_Score"]])
rfm["RFM_Score"] = (rfm["R_Score"].astype(str) + rfm["F_Score"].astype(str) + rfm["M_Score"].astype(str))
print(rfm[["Customer_ID","R_Score","F_Score","M_Score","RFM_Score"]])
rfm["M_Quantile"] = pd.qcut(
    rfm["Monetary"],
    q=5,
    labels=["Q1","Q2","Q3","Q4","Q5"]
)
print(rfm[["Customer_ID","Monetary","M_Quantile"]])
rfm["M_Bin"] = pd.cut(
    rfm["Monetary"],
    bins = 5,
    labels=["Q1","Q2","Q3","Q4","Q5"]
)
print(rfm[["Customer_ID","Monetary","M_Bin"]])
customer_sales = pd.pivot_table(
    completed_orders,
    values="Sales",
    index="Customer_ID",
    aggfunc="sum"
)
print(customer_sales)
sales_by_category=pd.pivot_table(
    completed_orders,
    values="Sales",
    index="Customer_ID",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)
print(sales_by_category)
average_order_value = monetary / frequency
print(average_order_value)

sorted_aov = average_order_value.sort_values(ascending=False)
print(sorted_aov)
sorted_aov = average_order_value.sort_values(ascending=False).head(3)
print(sorted_aov)