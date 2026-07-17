# pre processing ,labelEncoder 

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# data  import from  csv file : 

df = pd.read_csv("supervised machine learning\customer_data (1).csv")
# print(df)

# missing  value count : 
missing_value = df.isnull().sum()
# print(missing_value)


# missing value  fill  :  df.fillna() age --> mean ,salary --> median ,city,edu,purchased ---> mode 
# age ---> shlok  ,salary --> jenish , city edu pur --> prem 

df['Age'] =df['Age'].fillna(df['Age'].mean()).astype(int)
df['Salary'] =df['Salary'].fillna(df['Salary'].median()).astype(int)
df['City'] =df['City'].fillna(df['City'].mode()[0])
df['Education'] =df['Education'].fillna(df['Education'].mode()[0])
df['Purchased'] =df['Purchased'].fillna(df['Purchased'].mode()[0])

# label encode : 

le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df['Purchased'] = le.fit_transform(df['Purchased'])

# ordinal encode :  replace or map 

df['Education'] =(df['Education'].replace({'Graduate':1,'Post Graduate':2,'PhD':3}).astype(int))

# one hot encode :
city_encode = pd.get_dummies(df['City'],dtype=int)
df =pd.concat([df,city_encode],axis=1)
df=df.drop('City',axis=1)

# print(city_encode)
print(df)