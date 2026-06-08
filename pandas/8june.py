"""
pandas : 
1. data cleaning
2. data manipulation
3. data analysis
4. sorting , merge , join 
5. group by , filter 


ex : 
srno    name    department   salary 
1       John    HR           10000
2       Mary    HR           9000
3       Tom     IT           8000
4       jerry   Finance      7000

why pandas is  important for data analysis ?

pip install  pandas 
"""
# seris  : 1 dementaional data structure  
import pandas as pd
import numpy as np
"""data = pd.Series([1,2,3,4,5])
print(data)"""

# data1 = pd.Series([1,2,3,4,5,6,7],index=['a','b','c','d','e','f','g'])
"""
data1 = pd.Series([1,2,3,4,5,6,7],index=['rsm','sita','ravan','divy','elin','farana','green'])

print(data1)
print(data1.head())  # no  arg  ===> default 5  row 
print(data1.head(4))  # arg  ===> 4 
print(data1.tail())   # no arg  ===> last  5  row 
print(data1.tail(2))   # no arg  ===> last  5  row 
"""
# info , describe , describe (include ="all")

"""
data1 = pd.Series([1,2,3,4,5,6,7],index=['ram','sita','ravan','divy','elin','farana','green'])

print(data1)
print(data1.info())
print(data1.describe())
print(data1.describe(include='all'))
"""

# dataframe : 2 dementaional data structure

"""
2 way : 
1.list  : []
2.dict   : d1 = {23 : "che" , "phy" : 77}
"""

"""
df =pd.DataFrame({
    'id' :[1,2,3,4,5],
    'name' :['ram','sita','ravan','divy','elin'],
    'department' :['HR','IT','Finance','HR','Finance'],
    'salary' :[10000,9000,8000,7000,6000]
})

print(df)
"""
"""df1 =pd.DataFrame([
    [1,"ram","HR",90000],
    [2,"sita","IT",80000],
    [3,"ravan","Finance",70000],
    [4,"divy","HR",60000],
    [5,"elin","Finance",50000]
],columns=['id','name','department','salary'])
 
print(df1)
"""
# head ,tail , info , describe , describe (include ="all") ,print  only one  col , multiple col: 
df =pd.DataFrame({
    'id' :[1,2,3,4,5],
    'name' :['ram','sita','ravan','divy','elin'],
    'department' :['HR','IT','Finance','HR','Finance'],
    'salary' :[10000,9000,8000,7000,6000]
})

# print(df)
# print(df.head(3))
# print(df.tail(3)) 
# print(df.info())
# print(df.shape)
# print(df.columns)
# print(df.describe(include='all'))
# print(df.dtypes)

# print(df['name'])
print(df[['name','salary']])


# read_csv :
"""df = pd.read_csv("pandas\mckinsey.csv")
print(df)
"""