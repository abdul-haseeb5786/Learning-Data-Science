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

# -------------------------------------------------------------
# 📊 2. Series Attributes
# -------------------------------------------------------------
print("\nSeries Attributes:")
print("Size:", marks.size)
print("Data Type:", marks.dtype)
print("Index:", marks.index)
print("Values:", marks.values)
print("Is Unique:", marks.is_unique)

# -------------------------------------------------------------
# 🧩 3. Accessing Elements
# -------------------------------------------------------------
print("\nAccessing Elements:")
print("Single Element (by label):", marks['math'])
print("Multiple Elements (by labels):\n", marks[['math', 'urdu', 'science']])
print("Slicing:\n", marks[1:4])
print("Fancy Indexing:\n", marks[[0, 2, 4]])

# -------------------------------------------------------------
# ⚙️ 4. Mathematical & Statistical Operations
# -------------------------------------------------------------
print("\nMathematical Operations:")
print("Count:", marks.count())
print("Sum:", marks.sum())
print("Mean:", marks.mean())
print("Median:", marks.median())
print("Mode:\n", marks.mode())
print("Min:", marks.min())
print("Max:", marks.max())
print("Standard Deviation:", marks.std())
print("Variance:", marks.var())
print("\nDescriptive Statistics:\n", marks.describe())

# -------------------------------------------------------------
# 🔍 5. Sorting and Sampling
# -------------------------------------------------------------
print("\nSorting and Sampling:")
print("Sorted by Index:\n", marks.sort_index())
print("Sorted by Values:\n", marks.sort_values())
print("Random Sample (2 elements):\n", marks.sample(2))

# -------------------------------------------------------------
# 🧮 6. Boolean & Relational Operations
# -------------------------------------------------------------
print("\nBoolean Operations:")
print(marks > 80)
print("Marks greater than 80:\n", marks[marks > 80])

# -------------------------------------------------------------
# 🧠 7. Updating Series
# -------------------------------------------------------------
print("\nUpdating Values:")
marks['urdu'] = 82
marks['islamiyat'] = 95
print("Updated Series:\n", marks)

# -------------------------------------------------------------
# 🧰 8. Handling Missing Data
# -------------------------------------------------------------
marks['physics'] = None
print("\nWith Missing Value:\n", marks)
print("Is Null:\n", marks.isnull())
print("Fill Missing Values (with 0):\n", marks.fillna(0))
print("Drop Missing Values:\n", marks.dropna())

# -------------------------------------------------------------
# 🧾 9. Using Python Functions with Series
# -------------------------------------------------------------
print("\nUsing Python Functions:")
print("Length:", len(marks))
print("Type:", type(marks))
print("Minimum:", min(marks))
print("Maximum:", max(marks))
print("Sorted:\n", sorted(marks.dropna()))

# Convert to list and dictionary
print("\nAs List:", marks.tolist())
print("As Dictionary:", marks.to_dict())

# -------------------------------------------------------------
# 🧩 10. Important Series Methods
# -------------------------------------------------------------
print("\nImportant Series Methods:")
print("Unique Values:", marks.unique())
print("Value Counts:\n", marks.value_counts())
print("Duplicated Check:\n", marks.duplicated())
print("Drop Duplicates:\n", marks.drop_duplicates())
print("Data Type Conversion (to float):\n", marks.astype(float))
print("Check Membership:\n", marks.isin([90, 100]))
