# ---------------------------------------
# 📌 Data Visualization using Matplotlib
# ---------------------------------------

import numpy as np
import pandas as pd
from google.colab import drive
import matplotlib.pyplot as plt

plt.style.use('default')

# Mount Drive (for Colab only)
drive.mount('/content/drive')

# ---------------------------------------
# 1️⃣ LINE PLOTS (2D Line Plot)
# ---------------------------------------

batsman = pd.read_csv('/content/drive/MyDrive/python-Saylani/sharma-kohli.csv')

# Simple Line Plot (Numerical + Categorical)
plt.plot(batsman['index'], batsman['V Kohli'])
plt.plot(batsman['index'], batsman['RG Sharma'])
plt.title('Rohit Sharma Vs Virat Kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')
plt.grid()
plt.show()

# Custom style (colors + line styles)
plt.plot(batsman['index'], batsman['V Kohli'], color='#D9F10F', linestyle='solid')
plt.plot(batsman['index'], batsman['RG Sharma'], color='#FC00D6', linestyle='dashed')
plt.title('Customized Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')
plt.legend(['V Kohli', 'RG Sharma'], loc='upper right')
plt.grid()
plt.show()


# ---------------------------------------
# 2️⃣ SCATTER PLOTS
# ---------------------------------------

df = pd.read_csv('/content/drive/MyDrive/python-Saylani/batter.csv').head(50)

# Numerical vs Numerical Scatter Plot
plt.scatter(df['avg'], df['strike_rate'], color='red', marker='+')
plt.title('Avg vs Strike Rate of Top 50 Batsmen')
plt.xlabel('Average')
plt.ylabel('Strike Rate')
plt.show()

# Colored Scatter Plot using Iris data
iris = pd.read_csv('/content/drive/MyDrive/python-Saylani/iris.csv')
iris['Species'] = iris['Species'].replace({
    'Iris-setosa': 0,
    'Iris-versicolor': 1,
    'Iris-virginica': 2
})

plt.figure(figsize=(15, 7))
plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'], c=iris['Species'], alpha=0.7)
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.colorbar()
plt.title('Iris Dataset – Colored Scatter Plot')
plt.show()


# ---------------------------------------
# 3️⃣ SUBPLOTS
# ---------------------------------------

# 2x1 Subplots
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10, 6))
ax[0].scatter(df['avg'], df['strike_rate'], color='red')
ax[1].scatter(df['avg'], df['runs'])
ax[0].set_title('Avg vs Strike Rate')
ax[1].set_title('Avg vs Runs')
plt.show()

# 2x2 Subplots
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
ax[0, 0].scatter(df['avg'], df['strike_rate'], color='red')
ax[0, 1].scatter(df['avg'], df['runs'])
ax[1, 0].hist(df['avg'])
ax[1, 1].hist(df['runs'])
plt.show()


# ---------------------------------------
# 4️⃣ 3D SCATTER PLOT
# ---------------------------------------

fig = plt.figure(figsize=(6, 10))
ax = plt.subplot(projection='3d')
ax.scatter3D(df['runs'], df['avg'], df['strike_rate'])
ax.set_title('3D IPL Batsman Analysis')
ax.set_xlabel('Runs')
ax.set_ylabel('Avg')
ax.set_zlabel('Strike Rate')
plt.show()


# ---------------------------------------
# 5️⃣ BAR CHARTS
# ---------------------------------------

children = [10, 20, 40, 10, 30]
colors = ['red', 'blue', 'green', 'yellow', 'pink']

plt.bar(colors, children, color='black')
plt.title('Simple Bar Chart')
plt.show()

# Horizontal Bar Chart
plt.barh(colors, children, color='green')
plt.title('Horizontal Bar Chart')
plt.show()

# Multiple Bar Chart (Side-by-side)
df2 = pd.read_csv('/content/drive/MyDrive/python-Saylani/batsman_season_record.csv')

plt.bar(np.arange(df2.shape[0]) - 0.2, df2['2015'], width=0.2, color='yellow')
plt.bar(np.arange(df2.shape[0]), df2['2016'], width=0.2, color='red')
plt.bar(np.arange(df2.shape[0]) + 0.2, df2['2017'], width=0.2, color='blue')
plt.xticks(np.arange(df2.shape[0]), df2['batsman'], rotation='vertical')
plt.title('Seasonal Performance (Side-by-Side)')
plt.show()

# Stacked Bar Chart
plt.bar(df2['batsman'], df2['2017'], label='2017')
plt.bar(df2['batsman'], df2['2016'], bottom=df2['2017'], label='2016')
plt.bar(df2['batsman'], df2['2015'], bottom=df2['2016'] + df2['2017'], label='2015')
plt.legend()
plt.title('Stacked Bar Chart – Batsman Performance')
plt.xticks(rotation='vertical')
plt.show()


# ---------------------------------------
# 6️⃣ HISTOGRAM
# ---------------------------------------

vk = pd.read_csv('/content/drive/MyDrive/python-Saylani/vk.csv')

plt.hist(vk['batsman_runs'], bins=[0,10,20,30,40,50,60,70,80,90,100,110,120])
plt.xlabel('Runs')
plt.title('Virat Kohli Runs Distribution')
plt.show()


# ---------------------------------------
# 7️⃣ PIE CHART
# ---------------------------------------

data = [23, 45, 100, 20, 49]
subjects = ['English', 'Science', 'Maths', 'SST', 'Hindi']

plt.pie(data, labels=subjects, autopct='%0.1f%%')
plt.title('Subject Contribution')
plt.show()

# With real dataset
gayle = pd.read_csv('/content/drive/MyDrive/python-Saylani/gayle-175.csv')

plt.pie(gayle['batsman_runs'], labels=gayle['batsman'], autopct='%0.1f%%')
plt.title('Contribution in Gayle 175 Match')
plt.show()

