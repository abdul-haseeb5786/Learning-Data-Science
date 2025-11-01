# 🐼 Pandas - Day 1: Series
# Author: Abdul Haseeb
# Description: Introduction to Pandas Series with creation, attributes, methods, and indexing examples.

import pandas as pd

# -------------------------------------------------------------
# 📘 1. Creating a Series
# -------------------------------------------------------------

# From a list
marks = pd.Series([85, 90, 78, 92, 88])
print("📄 Series from List:\n", marks)

# From a list with custom index
marks = pd.Series([85, 90, 78, 92, 88], index=['math', 'english', 'urdu', 'science', 'history'])
print("\n📄 Series with Custom Index:\n", marks)

# From a dictionary
data = {'math': 85, 'english': 90, 'urdu': 78, 'science': 92, 'history': 88}
marks_dict = pd.Series(data)
print("\n📄 Series from Dictionary:\n", marks_dict)

# Assigning a name to Series
marks.name = "Student Marks"
print("\n🏷️ Series Name:", marks.name)
