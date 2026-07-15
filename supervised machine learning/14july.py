# supervised ML  : 
"""
| Area (sq ft) | Bedrooms | Age (Years) | Distance from City (km) | Price (₹ Lakhs) |
| ------------ | -------- | ----------- | ----------------------- | --------------- |
| 1000         | 2        | 10          | 8                       | 45              |
| 1500         | 3        | 5           | 6                       | 70              |
| 1800         | 3        | 2           | 5                       | 90              |
| 2200         | 4        | 1           | 3                       | 120             |
| 2800         | 5        | 1           | 2                       | 160             |

1.features label  : input variable 
2. output / target variable:  price  ===> output 
3. another  example : studyhrs,  attendance , assignment ,final  ===> marks
4. independent variable : variable not depend upon other variables  like .area , bedrooms , age , distance from city 
5. dependent variable  : its depend  upon other variables like price , marks , attendance. 
        
6. data set split 
    a.train set : 
    b.test set : 
    c.validation set 
    
7.overfitting  : model perform well on train set but not on test set.
8.underfitting : model perform poorly on test set and train set both. 

9.Bias      :
10.Variance : 

11.Practical 
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


df=pd.DataFrame({
    "area sqft":[1000,1500,1800,2200,2800],
    "bedrooms":[2,3,3,4,5],
    "age":[10,5,2,1,1],
    "distance from city":[8,6,5,3,2],
    "price":[45,70,90,120,160]
})

print(df)

X=df[['area sqft','bedrooms','age','distance from city']]
Y=df['price']

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

print("X_train",X_train)
print("X_test",X_test)
print("Y_train",Y_train)    
print("Y_test",Y_test)