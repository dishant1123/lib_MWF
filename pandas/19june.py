"""
1.isnull()  ===> check the  missing value  
2.isnull().sum() ===> missing value sum 
3. isna ()  ==>same as isnull 
4. isna().sum() ==> missing value  sum 
5. dropna ==> remove the  missing value   ,axis =1 that means col 
    print(df.dropna(how='all'))  # remove  row  when all value are missing
    print(df.dropna(thresh=4))  # 
    
6. fillna  ==> replace the missing value 
    df['age'] = df['age].fillna(df['age].mean())
    
7.forward fill ,backward fill : ffill , bfill  :
    df1["sales"] = df1["sales"].ffill()

8. MCAR (Missing Completely At Random)
"""
#dataframe : 
"""
2 ways  : 
1.dict 
2.list
"""
"""
id   name   age  salary
1     ram    45   90000
2     sita   40   80000
3     ravan  50   70000
"""

import  pandas as pd
import numpy as np
# using  dict : 
"""
df =pd.DataFrame({
    "id" :[101,102 ,103 ,104],
    "name" :["ram","sita","ravan","yug"],
    "age" :[45,40,50,20],
    "salary" :[90000,80000,70000,60000]
})
print(df)  # d1 = {"phy" : 90,"che" :78}   "phy" :[12,34,56,78]
print(df.shape)
"""
# using list : 
"""df1 =pd.DataFrame([
    [101,"ram",45,90000],
    [102,"sita",40,80000],
    [103,"ravan",50,70000],
    [104,"yug",20,60000]
],columns=["id","name","age","salary"])
print(df1)
print(df1.shape)"""

# missing value : 

"""
df =pd.DataFrame({
    "id" :[np.nan,102 ,103 ,104,np.nan],
    "name" :["ram",np.nan,"ravan",np.nan,"dhruv"],
    "age" :[np.nan,40,50,20,21],
    "salary" :[np.nan,np.nan,70000,60000,91000],
    "city" : ["delhi",'delhi',np.nan,"ahm","ahm"]
})

print(df)
"""
# method  : isnull, isna , isnull().sum() , isna().sum() 

"""
print(df.isna())
print(df.isna().sum())
print(df.isnull())
print(df.isnull().sum())
"""
# hw  diff between  isnull and isna :

# dropna (how , thresh , axis)  : remove  all missing value  

"""
print(df.dropna())   # default  rowise every  missing value 
print(df.dropna(axis =1))  # col wise  
print(df.dropna(how="all"))  # 
print(df.dropna(thresh=2)) 
"""

# fillna : replace the missing value  
"""df['age'] =df['age'].fillna(df['age'].mean())
df['city'] =df['city'].fillna(df['city'].mode()[1])

print(df)
"""

# forward fill , backward fill : ffill , bfill  :

"""df =pd.DataFrame({
    "id" :[np.nan,102 ,103 ,104,np.nan,np.nan],
    
})
print(df)
# df['id'] =df['id'].ffill()  # forward fill
df['id'] =df['id'].bfill()  # backward fill
print(df)
"""

# MCAR  : missing  completely  at  random
# MAR   : missing  at  random
# MNAR  : missing  not  at  random
