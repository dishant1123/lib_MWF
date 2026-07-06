"""
show  sns.load_dataset(iris)  , sns.load_dataset(tips)

1.pair plot  : use  sns.load_dataset(iris)
	Shows relationships between multiple numerical variables.
	Diagonal shows distributions.
	Off-diagonal shows scatter plots.
2.heat map :show the  coorelation between two num
3.relplot :Figure-level function used for relationship plots.
4.catplot :Figure-level categorical plot.
5.displot :Figure-level distribution plot.
6. jointplot :scatter + hist 
7.scatter +reg line  : shows relationship and best-fit line.
	Dots = actual observations
	Line = regression line
	Shaded region = confidence interval

"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# iris = sns.load_dataset('iris')
# tips = sns.load_dataset('tips')
# print(iris.head())
# print(tips.head(50))
# print(tips.tail(50))

# pair plot : 
"""
Shows relationships between multiple numerical variables.
Diagonal shows distributions.
Off-diagonal shows scatter plots.

df = sns.load_dataset("iris")
sns.pairplot(data=df, hue="species")

plt.show()

"""
# heat map  : 

"""
df = sns.load_dataset("tips")
corr =df[['total_bill','tip','size']].corr()
sns.heatmap(data=corr, annot=True, cmap="YlGnBu",fmt=".2f")
plt.show()
"""

# relplot :
"""
df = sns.load_dataset("tips")

sns.relplot(data=df, x="total_bill", y="tip", hue="day", col="time")
plt.show()
"""
# catplot :

"""
df = sns.load_dataset("tips")
sns.catplot(data=df, x="time", y="tip", hue="sex", kind="bar")
plt.show()
"""

# displot :
"""
df = sns.load_dataset("tips")
sns.displot(data=df, x="total_bill", hue="sex", kind="kde")
plt.show()
"""

# jointplot :

"""df=sns.load_dataset("tips")
sns.jointplot(data=df, x="total_bill", y="tip", hue="sex")
plt.show()
"""

# scatter + reg line :

df=sns.load_dataset("tips")
sns.regplot(data=df, x="total_bill", y="tip")
plt.show()