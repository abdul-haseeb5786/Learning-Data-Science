import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ✅ File ka local path
path = "healthcare-dataset-stroke-data.csv"
df = pd.read_csv(path)

# Overview
print("\n===== Original Dataset - First 10 Rows =====")
print(df.head(10))
print("\n===== Columns & Data Types =====")
print(df.dtypes)

# Missing values table
missing = df.isnull().sum().sort_values(ascending=False)
missing_percent = (df.isnull().mean()*100).sort_values(ascending=False)
missing_table = pd.concat([missing, missing_percent], axis=1)
missing_table.columns = ["Missing Count", "Missing Percent"]
print("\n===== Missing Values =====")
print(missing_table)

# Cleaning
clean = df.copy()

# Drop id
if "id" in clean.columns:
    clean = clean.drop(columns=["id"])

# Drop duplicates
clean = clean.drop_duplicates().reset_index(drop=True)

# Fill missing BMI values
if "bmi" in clean.columns:
    clean["bmi"] = pd.to_numeric(clean["bmi"], errors="coerce")
    medians_by_gender = clean.groupby("gender")["bmi"].median()
    overall_median = clean["bmi"].median()

    def fill_bmi(row):
        if pd.isnull(row["bmi"]):
            g = row["gender"]
            mg = medians_by_gender.get(g, np.nan)
            return mg if pd.notnull(mg) else overall_median
        else:
            return row["bmi"]

    clean["bmi"] = clean.apply(fill_bmi, axis=1)

# Convert object columns to category
cat_cols = clean.select_dtypes(include=["object"]).columns.tolist()
if "stroke" in cat_cols:
    cat_cols.remove("stroke")

for c in cat_cols:
    clean[c] = clean[c].astype("category")

# Smoking status
if "smoking_status" in clean.columns:
    if clean["smoking_status"].dtype.name == "category":
        if "Unknown" not in clean["smoking_status"].cat.categories:
            clean["smoking_status"] = clean["smoking_status"].cat.add_categories(["Unknown"])
    clean["smoking_status"] = clean["smoking_status"].fillna("Unknown")

# Cap outliers for numeric columns (IQR method)
def cap_outliers(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return series.clip(lower, upper)

if "avg_glucose_level" in clean.columns:
    clean["avg_glucose_level_capped"] = cap_outliers(clean["avg_glucose_level"])

if "bmi" in clean.columns:
    clean["bmi_capped"] = cap_outliers(clean["bmi"])

# Age groups
clean["age_group"] = pd.cut(
    clean["age"],
    bins=[0, 18, 35, 50, 65, 120],
    labels=["0-18", "19-35", "36-50", "51-65", "66+"],
)

# Save cleaned CSV (locally)
cleaned_path = "cleaned_healthcare_dataset.csv"
clean.to_csv(cleaned_path, index=False)

# --- EDA Plots ---
# 1 Age histogram
plt.figure(figsize=(8, 4))
plt.hist(clean["age"].dropna(), bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 2 Stroke count by gender
plt.figure(figsize=(6, 4))
gender_counts = clean.groupby("gender")["stroke"].sum()
gender_counts.plot(kind="bar")
plt.title("Number of Strokes by Gender")
plt.ylabel("Stroke Count")
plt.tight_layout()
plt.show()

# 3 Stroke rate by age_group
plt.figure(figsize=(8, 4))
stroke_rate_by_agegrp = clean.groupby("age_group")["stroke"].mean().sort_index()
stroke_rate_by_agegrp.plot(kind="bar")
plt.title("Stroke Rate by Age Group")
plt.ylabel("Stroke Rate")
plt.tight_layout()
plt.show()

# 4 Age vs Avg Glucose Level scatter
plt.figure(figsize=(7, 5))
plt.scatter(clean["age"], clean["avg_glucose_level"], alpha=0.6)
plt.title("Age vs Avg Glucose Level")
plt.xlabel("Age")
plt.ylabel("Avg Glucose Level")
plt.tight_layout()
plt.show()

# 5 Correlation matrix heatmap
num_df = clean.select_dtypes(include=[np.number]).copy()
corr = num_df.corr()
plt.figure(figsize=(8, 6))
plt.imshow(corr, interpolation="nearest", aspect="auto")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Matrix (Numerical Features)")
plt.tight_layout()
plt.show()

# 6 Stroke rate by smoking_status
if "smoking_status" in clean.columns:
    plt.figure(figsize=(8, 4))
    s = clean.groupby("smoking_status")["stroke"].mean().sort_values(ascending=False)
    s.plot(kind="bar")
    plt.title("Stroke Rate by Smoking Status")
    plt.ylabel("Stroke Rate")
    plt.tight_layout()
    plt.show()

print("\n===== Cleaned Dataset - First 10 Rows =====")
print(clean.head(10))
print("\nCleaned CSV saved as:", cleaned_path)
print("\n✅ All plots displayed successfully!")

