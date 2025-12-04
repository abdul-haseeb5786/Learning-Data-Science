# SEABORN PRACTICE — DAY 1
# Author: Your Name
# Description:
# This file covers Seaborn basics, including:
# relational plots, distribution plots, categorical plots,
# multiplots, facet grids, and pairwise visualizations.

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# -------------------------
# Dataset Loading
# -------------------------
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
gap = px.data.gapminder()

# -------------------------
# 1. RELATIONAL PLOTS
# -------------------------

# Scatterplot (axes-level)
sns.scatterplot(data=tips, x='total_bill', y='tip',
                hue='sex', style='time', size='size')
plt.show()

# Scatter using relplot (figure-level)
sns.relplot(data=tips, x='total_bill', y='tip',
            kind='scatter', hue='sex', style='time', size='size')
plt.show()

# Lineplot for Pakistan trend
pak = gap[gap['country'] == 'Pakistan']

sns.lineplot(data=pak, x='year', y='lifeExp')
plt.show()

sns.relplot(data=pak, x='year', y='lifeExp', kind='line')
plt.show()

# Multiple country comparison
multi = gap[gap['country'].isin(['Germany', 'Pakistan', 'Brazil'])]

sns.relplot(kind='line', data=multi, x='year', y='lifeExp',
            hue='country', style='continent', size='continent')
plt.show()

# Facet plot
sns.relplot(data=tips, x='total_bill', y='tip',
            kind='line', col='sex', row='day')
plt.show()

# -------------------------
# 2. DISTRIBUTION PLOTS
# -------------------------

# Histogram
sns.histplot(data=tips, x='total_bill')
plt.show()

# Displot figure-level histogram
sns.displot(data=tips, x='total_bill', kind='hist')
plt.show()

# KDE plot
sns.kdeplot(data=tips, x='total_bill')
plt.show()

sns.displot(data=tips, x='total_bill', kind='kde', hue='sex', fill=True)
plt.show()

# -------------------------
# 3. CATEGORICAL PLOTS
# -------------------------

# Stripplot
sns.stripplot(data=tips, x='day', y='total_bill')
plt.show()

sns.catplot(data=tips, x='day', y='total_bill', kind='strip', jitter=0.3)
plt.show()

# Swarmplot
sns.swarmplot(data=tips, x='day', y='total_bill')
plt.show()

# Boxplot
sns.boxplot(data=tips, x='day', y='total_bill', hue='sex')
plt.show()

# Violinplot
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', split=True)
plt.show()

# Barplot
sns.barplot(data=tips, x='sex', y='total_bill')
plt.show()

# Countplot
sns.countplot(data=tips, x='sex', hue='day')
plt.show()

# -------------------------
# 4. MULTIPLOT — FacetGrid
# -------------------------
g = sns.FacetGrid(data=tips, col='day', row='time', hue='smoker')
g.map(sns.scatterplot, 'sex', 'total_bill')
g.add_legend()
plt.show()

# -------------------------
# 5. PAIRWISE PLOTTING
# -------------------------

# Pairplot
sns.pairplot(iris, hue='species')
plt.show()

# PairGrid customized
g = sns.PairGrid(iris, hue='species')
g.map_diag(sns.boxplot)
g.map_offdiag(sns.scatterplot)
plt.show()

