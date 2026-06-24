
"""
1. Winsorization is an outlier treatment technique where extreme values are replaced with less extreme values instead of deleting the rows.

2. convert object  to numeric : to_numeric
3.convert string to bool 
4. detect the duplicates 
5. value_counts
6. remove  duplicated  : drop_duplicates
7. replace  
8. string  to date_time  :pd.to_datetime  : year  month days month_name

"""
# datetime  : 
import pandas as pd 

"""
df =pd.DataFrame({
    "id" :[1,2,3,4,5,6,7],
    "name" :["ram","sita","ravan","laxman","surekha","ravi","ramesh"],
    "joining_date":["2020-01-03","2020-02-10","2020-03-11","2020-04-15","2020-05-16","2020-06-12","2020-07-19"]
})

# print(df)
# print(df.dtypes)
df['joining_date'] = pd.to_datetime(df['joining_date'])

df["year"]=df['joining_date'].dt.year
df["days"]=df['joining_date'].dt.day
df["month"]=df['joining_date'].dt.month_name()
df['today'] =pd.Timestamp.now()
print(df)
"""

# convert : 

df =pd.DataFrame({
    "id" :[1,2,3,4,5,6,7],
    "name" :["ram","sita","ravan","laxman","surekha","ravi","ramesh"],
    "status" :["True","False","True","False","True","False","True"],
    "experience":["2","4","1","5","7","9","3"],
    "city" :["ahm","ahmedabad","bombay","mumbai","delhi","pune","rajstan"]
})
df['experience'] = pd.to_numeric(df['experience'])
print(df.dtypes)

df['status'] = df['status'].map({
    "True":True,
    "False":False
})
print(df.dtypes)

# string  : 

# df['name'] =df['name'].str.upper()
# df['name'] =df['name'].str.title()
# df['city'] =df['city'].str.replace(
    # "ahm","ahmedabad")
df['city'] =df['city'].replace(['ahm',"bombay"],["ahemedabad","mumbai"])

print(df)

# pending  topic : duplicate ,Winsorization,loc ,iloc ,join, groupby ,concat ,filter ,pivort_table,sort ,apply,get_dummies , which  data type  we use to fill means mean ,avg how to decided 
