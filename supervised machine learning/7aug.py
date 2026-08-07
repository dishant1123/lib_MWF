#California Housing Data
"""
step :1 read csv 
step :2 explore  data check the  missing  values 
step :3 handle missing values :fill with median
step :4 encode : get_dummies() ----> ocean_proximity
step :5 features (X) and target (y)
step :6 train-test split
step :7 scaler 
srep :8 model :
    simple linear regression ----> 1 feature only ---> income vs house value
    multiple linear regression ----> all features
    ridge regression ----> l2 --->alpha=1
    lasso regression ----> l1 --->alpha=100 ,max_iter=10000
    elasticnet ----> l1 + l2 --->alpha=1 ,l1_ratio=0.5 ,max_iter=10000
step :9 compare all models
    
Try : CAR DETAILS FROM CAR DEKHO.csv ,Medical Cost Personal Datasets.csv
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error,mean_absolute_percentage_error

# read data :
df =pd.read_csv("supervised machine learning/housing.csv")
# print(df.head())

# data  explore , missing  values : 
"""print(df.info())
missing_values =df.isnull().sum()
print(missing_values)
"""
df['total_bedrooms']=df['total_bedrooms'].fillna(df['total_bedrooms'].median()) 
"""
missing_values =df.isnull().sum()
print(missing_values)
"""

# get dummies : 
df =pd.get_dummies(df,columns=['ocean_proximity'],drop_first=True)
# print(df.head())
# features and target :

X =df.drop(['median_house_value'],axis=1)
y =df['median_house_value']

# split data :
X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42)

# scaler :
scaler = StandardScaler()
X_scaler=scaler.fit_transform(X_train,y_train)
x_test_scaler=scaler.transform(X_test)

# function  : 
"""
evaluation  :  1. r2score 2. mean_squared_error 3. mean_absolute_error 4. mean_absolute_percentage_error
arg ---->2 

"""

# model :  1. simple linear regression 
x_linear = df[['median_income']]
y_linear = df['median_house_value'] 

x_linear_train,x_linear_test,y_linear_train,y_linear_test=train_test_split(
    x_linear,
    y_linear,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(x_linear_train,y_linear_train)
pred=model.predict(x_linear_test)

print("coefficient :",model.coef_[0])
print("intercept :",model.intercept_)
# print("r2_score linear :",r2_score(y_linear_test,pred))

# model : 2. multiple linear regression

multi = LinearRegression()
multi.fit(X_train,y_train)
pred=multi.predict(X_test)
# print("r2_score multiple linear :",r2_score(y_test,pred))

# model : 3. lasso
l1 = Lasso(alpha=100,max_iter=10000)
l1.fit(X_scaler,y_train)
pred=l1.predict(x_test_scaler)

# print("r2_score lasso :",r2_score(y_test,pred))

# model : 4. ridge

r1=Ridge(alpha=1)
r1.fit(X_scaler,y_train)
pred=r1.predict(x_test_scaler)
# print("r2_score ridge :",r2_score(y_test,pred))

# model : 5. elasticnet
e1=ElasticNet(alpha=1,l1_ratio=0.5,max_iter=10000) 
e1.fit(X_scaler,y_train)
pred=e1.predict(x_test_scaler)
# print("r2_score elasticnet :",r2_score(y_test,pred))

# compare all models :

print("r2_score linear :",r2_score(y_linear_test,pred))
print("r2_score multiple linear :",r2_score(y_test,pred))
print("r2_score lasso :",r2_score(y_test,pred))
print("r2_score ridge :",r2_score(y_test,pred))
print("r2_score elasticnet :",r2_score(y_test,pred))