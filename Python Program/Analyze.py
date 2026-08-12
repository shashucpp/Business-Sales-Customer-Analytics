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

print("Total Revenue = ",np.sum(sales["Total_Sales"]))

print("Average = ",np.mean(sales["Total_Sales"]))

print("median = ",np.median(sales["Total_Sales"]))

print("Maximum = ",np.max(sales["Total_Sales"]))

print("Minimum = ",np.min(sales["Total_Sales"]))

print("Deviation = ",np.std(sales["Total_Sales"]))

print("Variance = ",np.var(sales["Total_Sales"]))

print("Mean = ",np.mean(sales["Quantity"]))

print("Median = ",np.median(sales["Quantity"]))

print("Standard Deviation = ",np.std(sales["Quantity"]))

print(np.ptp(sales["Total_Sales"]))

print(np.sum(sales["Total_Sales"] > 50000))

high = np.where(sales["Total_Sales"] > 100000)

print(sales.iloc[high])

sales = np.sort(sales["Total_Sales"])

growth = np.diff(sales)

print(growth)