"""
EDA : Exploratory Data Analysis

EDA :
| Topic                     | Purpose                                             | Common Functions/Plots                 |
| ------------------------- | --------------------------------------------------- | -------------------------------------- |
| **EDA**                   | Understand and prepare data                         | info(), describe(), isnull()     |
| **Univariate Analysis**   | Analyze one variable                                | Histogram, Box Plot, Count Plot        |
| **Bivariate Analysis**    | Analyze relationship between two variables          | Scatter Plot, Correlation, groupby() |
| **Multivariate Analysis** | Analyze relationships among three or more variables | Pairplot, Heatmap                      |
| **Data Patterns**         | Detect trends, seasonality, clusters, and outliers  | Histograms, Box Plots, Scatter Plots   |
| **Feature Relationships** | Measure how variables relate to each other          | Correlation Matrix, Heatmap            |


"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


data= sns.load_dataset("tips")
print(data.head())

# step  1 : info () ,describe() ,head() ,tail() ,isnull().sum() 

"""
print(sns.info())
print(sns.describe())
print(sns.head(2))
print(sns.tail(2))
print(sns.isnull().sum())
"""

#step 2 : Univariate Analysis  : Histogram , Box Plot , Count Plot

# frequency :
"""plt.hist(data=sns,x="total_bill",bins=5)
plt.title("Histogram of total_bill")
plt.show()
"""
# outlier detection :  box plot 
"""sns.boxplot(data=data,x="total_bill")
plt.show()
"""
#count plot : 
"""sns.countplot(data=data,x="sex")
plt.show()

print(data['sex'].value_counts())
print(data['smoker'].value_counts())
"""

#Bivariate Analysis : scatter plot  , coorelation  , groupby

"""sns.scatterplot(data=data,x="total_bill",y="tip")
plt.show()
"""
sns.heatmap(data =data.corr(numeric_only=True),annot=True,cmap="YlGnBu",fmt=".2f")
plt.show()
