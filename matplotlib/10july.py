"""
1. pd.get_dummies()
2. image  analysis using numpy 
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

print(picture)
print(picture.shape)

# inverted_picture =picture[ : : -1,:,:]
# mirror_image =picture[ :,: :-1,:]
# reduce_qulity =picture[ :,:, : :-1]
crop_image=picture[30 :190,150 :550,0:200 ] 
plt.imshow(crop_image)
plt.show()
