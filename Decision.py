import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style="whitegrid")
plt.style.use("ggplot")

all_sheets = pd.read_excel("Final.xlsx",sheet_name=None)

sales = all_sheets["Sales"]
customers = all_sheets["Customer"]
products = all_sheets["Product"]

#Customer Segmentation

sales["Customer_Type"] = np.select(
    [
        sales["Unit_Price"] >= 100000,
        sales["Unit_Price"] >= 50000
    ],
    [
        "Premium",
        "Gold"
    ],
    default="Regular"
)

#Inventory Analysis

products["Inventory_Status"] = np.where(
    products["Stock_Quantity"] <= products["Reorder_Level"],
    "Reorder",
    "Available"
)

#Revenue

sales["Revenue"] = (sales["Unit_Price"] * sales["Total_Sales"])

#Revenue Contribution

sales["Contribution"] = (
    sales["Revenue"] /
    np.sum(sales["Revenue"])
) * 100

with pd.ExcelWriter(
    "Finals.xlsx",
    engine="openpyxl"
) as writer:

    customers.to_excel(
        writer,
        sheet_name="Customer",
        index=False
    )

    sales.to_excel(
        writer,
        sheet_name="Sales",
        index=False
    )

    products.to_excel(
        writer,
        sheet_name="Product",
        index=False
    )

print("✅ All cleaned sheets exported successfully!")