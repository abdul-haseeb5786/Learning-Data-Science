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
