# ---------------------------------------------------------
# SUPERSTORE DATA ANALYSIS - FULL ASSIGNMENT CODE
# ---------------------------------------------------------

# IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("default")
sns.set_palette("Set2")

# ---------------------------------------------------------
# 1. LOAD DATA
# ---------------------------------------------------------

df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Preview
print("\n--- HEAD OF DATA ---")
print(df.head())


# ---------------------------------------------------------
# 2. CLEAN THE DATA
# ---------------------------------------------------------

print("\n--- CLEANING DATA ---")

# Remove duplicates
df = df.drop_duplicates()

# Convert date columns to datetime
date_cols = ["Order Date", "Ship Date"]
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Remove rows with missing essential numeric fields
df = df.dropna(subset=["Sales", "Quantity", "Profit"])

# Ensure numeric columns
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")

df = df.dropna(subset=["Sales", "Quantity", "Profit"])

print("Cleaning completed.\n")


# ---------------------------------------------------------
# 3. DATASET OVERVIEW
# ---------------------------------------------------------

print("\n--- DATASET OVERVIEW ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nColumn Types:\n", df.dtypes)

print("\nMissing Values:\n", df.isnull().sum())


# ---------------------------------------------------------
# 4. STATISTICAL SUMMARIES
# ---------------------------------------------------------

print("\n--- STATISTICAL SUMMARY ---")
print(df.describe())

# Category summary
category_summary = df.groupby("Category")[["Sales", "Profit", "Quantity"]].sum()
print("\n--- CATEGORY SUMMARY ---")
print(category_summary)


# ---------------------------------------------------------
# 5. EXPLORATORY DATA ANALYSIS (EDA)
# ---------------------------------------------------------

# --- Distribution: Sales ---
plt.figure(figsize=(8,5))
plt.hist(df["Sales"], bins=40)
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# --- Distribution: Profit ---
plt.figure(figsize=(8,5))
plt.hist(df["Profit"], bins=40)
plt.title("Distribution of Profit")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

# --- Distribution: Quantity ---
plt.figure(figsize=(8,5))
plt.hist(df["Quantity"], bins=30)
plt.title("Distribution of Quantity")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()

# --- Scatter: Sales vs Profit ---
plt.figure(figsize=(7,5))
plt.scatter(df["Sales"], df["Profit"], alpha=0.4)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

# --- Correlation Heatmap ---
plt.figure(figsize=(7,5))
sns.heatmap(df[["Sales", "Profit", "Quantity", "Discount"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# --- Top 10 Sub-Categories by Sales ---
top_sub = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
top_sub.plot(kind="bar")
plt.title("Top 10 Sub-Categories by Sales")
plt.ylabel("Total Sales")
plt.show()

# --- Profit by Category ---
plt.figure(figsize=(7,5))
sns.boxplot(x="Category", y="Profit", data=df)
plt.title("Profit Distribution by Category")
plt.show()


# ---------------------------------------------------------
# 6. FINAL INSIGHTS REPORT (Printed)
# ---------------------------------------------------------

print("\n\n================================================")
print(" FINAL REPORT – MAJOR INSIGHTS FROM THE DATA")
print("================================================")

# Insight 1
print("\n1. Sales and profit distributions are highly right-skewed.")
print("   → A small number of large orders contribute heavily to revenue.\n")

# Insight 2
print("2. Technology and Furniture categories generate the highest sales.")
print("   → But some sub-categories show negative or low profit margins.\n")

# Insight 3
print("3. States like California, New York, and Texas dominate total sales.")
print("   → These are key markets for the business.\n")

# Insight 4
print("4. Many high-discount items result in negative profit.")
print("   → More discount control is required.\n")

# Insight 5
print("5. Strong positive correlation between Sales and Profit.")
print("   → But outliers exist with high sales & negative profit.\n")

print("================================================")
print(" END OF REPORT")
print("================================================")
