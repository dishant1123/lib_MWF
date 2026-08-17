"""
1. pd.get_dummies()  ===> done 
2. image  analysis using numpy   ===> done 
3. EDA : using sample  super store 
4. SQL  connectivity  : using import pymysql sqlalchemy
 
EDA : 
step :1 load data set  
step :2 basic exploration  : head tail describe info shape columns 
step :3 missing value  : isnull()
step :4 duplicates  : df.duplicated().sum() then df =df.drop_duplicates()
step :5 convert date into  pd.to_datetime()  ==> like  order_date, ship_date
step :6 auto EDA  : pip install ydata-profiling 

step :7  pip install sweetviz  ===> function  : sv.analyze(df)
"""
# business related case study  : 
"""
1.sales ===> mean , avg  , sum  , min  , max  
2. top 10 sales : using  nlargest() 

3. profit  :
4. customer segement  behaviour  : segement  wise  
5. discount vs profit 
6. city , region, state  wise  performance : sales , profit  
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

from ydata_profiling import ProfileReport
"""

df=pd.DataFrame({
    "id" :[1,2,3,4,5],
    "name":["saloni","dhruvi","vijay","jay","raj"],
    "age":[24,25,27,28,29],
    "gender":["female","female","male","male","male"],
    "salary":[1000,2000,3000,4000,5000],
})
"""
# print(df)

# pd.get_dummies()

"""dummies =pd.get_dummies(df,columns=["gender"],drop_first=True,dtype=int)
print(dummies)
"""

# image analysis using  :
picture =plt.imread("matplotlib/virat_rohit.jpg")

# print(picture)
print(picture.shape)

inverted_picture =picture[ : : -1,:,:]
# mirror_image =picture[ :,: :-1,:]
# reduce_qulity =picture[ :,:, : :-1]
# crop_image=picture[30 :190,150 :550,0:200 ] 
plt.imshow(inverted_picture)
plt.show()


"""df =pd.read_csv("matplotlib\SampleSuperstore.csv")
print(df.head())
"""
"""
report = ProfileReport(df, title="Superstore Sales Report", explorative=True)  #check  explorative 
report.to_file("Superstore_Sales_Report.html")
"""
"""import sweetviz as sv

report  = sv.analyze(df)
report.show_html("sample.html")

"""

# hw : dtale() 

# pip install  pymysql sqlalchemy , mysql-connector-python,psycopg2 

"""from sqlalchemy import create_engine

username="root"
password="root"
host="localhost"
port=3306
database="employees"

create_engine1 = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

df =pd.read_sql("select * from emp",con=create_engine1)
print(df.head())
"""

"""s1="flipkart-Sale-2024"

print(s1.lower())
print(s1.replace("-"," ",1))
"""

"""
n=int(input("enter number"))
d1={}

for i in range(n):
    follower =input("enter follower")
    value=int(input("enter the value :)) 
    d1[follower] =value
print(d1)
"""
"""
def split_product_code(product_code):
    return product_code.split()


product_code = 'ZOMATO-FOOD-2024'
result = split_product_code(product_code)
print(result)"""