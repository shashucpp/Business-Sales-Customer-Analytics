import pandas as pd
import numpy as np

all_sheets = pd.read_excel("industry_level_raw_messy_business_data.xlsx",sheet_name=None)

sales = all_sheets["Raw_Sales_Data"]
customers = all_sheets["Raw_Customer_Master"]
products = all_sheets["Raw_Product_Master"]

#print(sales)
#print(customers)
#print(products)

#print(sales.columns)
#print(customers.columns)
#print(products.columns)


# Clean and modify the Sales DataFrame

sales = sales.sort_values(
    by="Customer_ID",
    ascending=True
)

sales["Customer_Name"] = sales["Customer_Name"].str.strip()

sales["Email"] = sales["Email"].fillna("Unknown").str.lower().str.strip()

sales["Phone"] = sales["Phone"].fillna("Not Available")

sales["City"] = sales["City"].str.lower()

sales["State"] = sales["State"].str.lower()

sales["Quantity"] = sales["Quantity"].abs()

sales["Total_Sales"] = sales["Total_Sales"].astype(float)

sales["Unit_Price"] = sales["Unit_Price"].astype(float)

sales["Quantity"] = sales["Quantity"].astype(int)

sales["Unit_Price"] = sales["Unit_Price"].fillna(0)

#print(sales)

#Customer Data

customers = customers.sort_values(
    by="Customer_ID",
    ascending=True
)

customers["Customer_Name"] = customers["Customer_Name"].str.strip()

customers["Email"] = customers["Email"].fillna("Unknown").str.lower().str.strip()

customers["Phone"] = customers["Phone"].fillna("Not Available")

customers["City"] = customers["City"].str.lower()

customers["State"] = customers["State"].str.lower()

customers.rename(columns = {"Registration_Date":"Registeration_Date"},inplace="True")

customers["Registeration_Date"].astype(str)

customers["Registeration_Date"] = pd.to_datetime(
    customers["Registeration_Date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

#print(customers)

products["Standard_Price"] = products["Standard_Price"].astype(float)

products["Reorder_Level"] = products["Reorder_Level"].astype(int)

products["Stock_Quantity"] = products["Stock_Quantity"].astype(int)


with pd.ExcelWriter(
    "Final.xlsx",
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