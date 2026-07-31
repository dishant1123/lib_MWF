# polynomial regression : 
"""
What is Polynomial Regression?
Definition :Polynomial Regression is an extension of Linear Regression that models non-linear relationships between the independent variable (X) and dependent variable (Y).

Instead of fitting a straight line,
y=b0+b1x
y=b0+b1x+b2x2
y=b0+b1x+b2x2+b3x3

Although the equation looks non-linear, it is still considered Linear Regression because it is linear in the coefficients.

When the relationship between input and output is non-linear, Polynomial Regression can model the curve better than Linear Regression.

PolynomialFeatures() :It generates additional polynomial features from the original input features, such as squares and cubes.
"""

# ex :1 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error,r2_score,root_mean_squared_error


df =pd.read_csv("supervised machine learning/car_braking_distance.csv")
print(df)

plt.plot(df['Speed'],df['BrakingDistance'])
plt.xlabel('Speed')
plt.ylabel('Braking Distance')
plt.title('Braking Distance vs Speed')
plt.show()

# feature : 
X=df[['Speed']]
y=df['BrakingDistance']

#model : 
model = LinearRegression()
model.fit(X,y)
y_predict = model.predict(X)

# polynomial features :
model = LinearRegression()
x_poly = PolynomialFeatures(degree=2)
fit =x_poly.fit_transform(X)
model.fit(fit,y)

# prediction  : 
y_pred1 = model.predict(fit)
print("predicted value :",y_pred1) 

# comparison :   actual value and  predicted value
comparison = pd.DataFrame({'Actual value':y.values,
                           'Predicted value':y_pred1})

# graph : 
"""
1. linear regression
2. polynomial regression
"""
