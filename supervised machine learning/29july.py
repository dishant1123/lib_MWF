"""
yrs of exp   actual   predict     loss    MSE 

2            35000    34670       330     108900
3            42000    43600      -1600    2560000
5            52000    51800       200     40000

MSE  :902967 
RMSE :950 
MAE : 710
R2 score =  total  loss (square) : 2708900 , mean actual  : 43000  

            sigma(actual -mean) **2   =====> ss_total  
            
r2 score = 0.98  
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error,r2_score,root_mean_squared_error

df = pd.read_csv("supervised machine learning/salary_data (1).csv")
print(df)

# scatter plot :
plt.figure(figsize=(10,6))
plt.scatter(
    df['YearsExperience'],
    df['Salary'],
    color='blue'
)
plt.title('Salary vs Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.grid(True)
# plt.show()

# features selection  : 
X=df[['YearsExperience']]
y=df['Salary']

# split data : 
X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,   # 80 % train 20 % test
    random_state=42
)
"""
x_train ====> input features  exp 
y_train ====> output value  salary  actual value 
x_test  ====> 4.5
y_test  ====> 45000 

ex :

train
1   34
2   46
3   45 
4   68
5   70
6   75
7   80
8   85

test :
9    90
10   95
11   100 

"""

# create model : 
model = LinearRegression()

# train model :
model.fit(X_train,y_train) 

# slope , intercept :
print("model slope :",model.coef_[0])
print("model intercept :",model.intercept_)

# prediction  : 
y_pred = model.predict(X_test)
print("predicted value :",y_pred) 

# comparison :   actual value and  predicted value
comparison = pd.DataFrame({'Actual value':y_test.values,
                           'Predicted value':y_pred})

print(comparison)

# evaluation :  mean square error
# regression  line  :  actual , predict 
plt.figure(figsize=(10,6))

plt.scatter(
    X,
    y,
    color='blue',
    label='Actual value'
    
)
plt.plot(
    X,
    model.predict(X),
    color='red',
    label='regression line'
)
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs Years of Experience')
plt.legend()
plt.grid(True)
# plt.show()

# predict new  data  : 

exper = [[7.5]]
predict_salary = model.predict(exper)
print("predict salary :",predict_salary[0])

# hw  : 
"""
apply evaluation metrics  in above  code  ====> salary_data (1).csv
apply evaluation metrics  in above  code  ====> student_marks_small .csv 


traning score  = model.score(X_train,y_train)
testing score  = model.score(X_test,y_test)

overfitting 
underfitting

"""

