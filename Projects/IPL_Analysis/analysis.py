# 🏏 IPL Data Analysis
# Author: Abdul Haseeb

# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('IPL_Matches.csv')

# Display first few rows
print("📄 Dataset Preview:")
print(df.head())

# Basic info
print("\n📊 Dataset Info:")
print(df.info())

# Check for missing values
print("\n🔍 Missing Values:")
print(df.isnull().sum())

# --- Data Analysis ---

# 1️⃣ Most successful teams
top_teams = df['winner'].value_counts().head(5)
print("\n🏆 Top 5 Teams by Wins:")
print(top_teams)
