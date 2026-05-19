import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/superstore.xls.csv", encoding="latin1")

# First 5 rows
print("FIRST 5 ROWS")
print(df.head())

# Dataset information
print("\nDATASET INFO")
print(df.info())

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Total Sales
total_sales = df["Sales"].sum()
print("\nTOTAL SALES:", round(total_sales, 2))

# Total Profit
total_profit = df["Profit"].sum()
print("TOTAL PROFIT:", round(total_profit, 2))

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSALES BY CATEGORY")
print(category_sales)

# Profit by Region
region_profit = df.groupby("Region")["Profit"].sum()

print("\nPROFIT BY REGION")
print(region_profit)

# Top 10 Sub-Categories
top_products = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 SUB-CATEGORIES")
print(top_products)

# ----------------------------
# PIE CHART - Sales by Category
# ----------------------------

plt.figure(figsize=(7, 7))

category_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Sales Distribution by Category")
plt.ylabel("")
plt.tight_layout()
plt.show()


# ----------------------------
# BAR CHART - Profit by Region
# ----------------------------

plt.figure(figsize=(8, 5))

region_profit.plot(kind="bar")

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ----------------------------
# HORIZONTAL BAR CHART - Top 10 Sub-Categories
# ----------------------------

plt.figure(figsize=(9, 6))

top_products.plot(kind="barh")

plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sales")
plt.ylabel("Sub-Category")

plt.tight_layout()
plt.show()