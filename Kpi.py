import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style="whitegrid")
plt.style.use("ggplot")

all_sheets = pd.read_excel("Finals.xlsx",sheet_name=None)

sales = all_sheets["Sales"]

# KPIs

total_revenue = sales["Revenue"].sum()

total_customers = sales["Customer_ID"].nunique()

total_orders = sales["Customer_ID"].nunique()

average_order_value = total_revenue / total_orders

total_quantity = sales["Quantity"].sum()

highest_sale = sales["Revenue"].max()

lowest_sale = sales["Revenue"].min()

# Display Kpis Cards

print("="*50)
print(f"Total Revenue      : ₹{total_revenue:,.2f}")
print(f"Total Orders       : {total_orders}")
print(f"Total Customers    : {total_customers}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")
print(f"Total Quantity     : {total_quantity}")
print(f"Highest Sale       : ₹{highest_sale:,.2f}")
print(f"Lowest Sale        : ₹{lowest_sale:,.2f}")
print("="*50)

# Store Kpi in Dataframe

kpi = pd.DataFrame({
    "KPI": [
        "Total Revenue",
        "Total Orders",
        "Total Customers",
        "Average Order Value",
        "Total Quantity"
    ],
    "Value": [
        total_revenue,
        total_orders,
        total_customers,
        average_order_value,
        total_quantity
    ]
})

kpi.to_excel("KPI_Report.xlsx", index=False)