# pandas : pip intall pandas 
"""
1. data  cleanning 
2. data manipulation 
3. data analysis
4. sorting , merge , join,concat 

# file  ===> read  ===>csv,excel ,tsv ,json 

data  : 
1. seris   : 1d structure data [12,45,67,89]
2. dataframe  : 2d structure data
    ex : 
    id   name salary 
    1    ram   10000
    2    sita  9000
    3    ravan 8000

"""

# seris : 
import pandas as pd
import numpy as np
"""
a=pd.Series([10,27,38,49,52,60])
print(a)

b= pd.Series([12.56,78.90,34.90],index=['a','b','c'])
print(b)

c=pd.Series(["ram","sita","ravan"],index =[1,2,3])
print(c)

d=pd.Series({12:90,"math":80,"comp":70})
print(d)
"""
# head , tail ,info ,describe ,describe(include =all)

"""a=pd.Series([10,27,38,49,52,60,89,78,67,45,12,np.nan])
print(a)
print(a.head())  #no arg  ===> default 5 row
print(a.head(3))
print(a.tail())  # no arg  ===> last 5 row
print(a.tail(3))  # last 3 row
print(a.shape)
print(a.info())
print(a.describe())
"""

# read_csv function  : 
"""df = pd.read_csv("pandas\student.csv")
print(df)
print(df.head(2))
print(df.tail(4))
print(df.info())
print(df.describe(include='all'))
"""
# df = pd.read_csv("pandas\student1.tsv",sep='\t')
# print(df)

# hw : json read , excel read ,

