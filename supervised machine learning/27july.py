"""
multiple linear regression :1 continuous dependent variable  using two or more independent variable.

	y =b0 +b1x1+b2x2 +....+bnxn  

y =depe , x1x2 = indepe ,b0= intercept  ,b1b2 =coefficients 

========================================
interpretations  of  coeff :

| Feature  | Coefficient |
| -------- | ----------- |
| Area     | 150         |
| Bedrooms | 12000       |
| Age      | -2500       |

Area = 150
1000 sqft
↓
1001 sqft
Price increases by ₹150

Bedrooms = 12000
Every additional bedroom increases price by ₹12,000, assuming Area and Age remain constant.

2 Bedrooms
↓
3 Bedrooms

Price increases by ₹12,000

Age = -2500
Every additional year decreases price by ₹2,500.
House Age = 10
↓
House Age = 11
Price decreases by ₹2,500

============================================

multicollinearity :two or more indep variable highly correlated with each other. 
ex: area ----> number  of rooms ----> window 
means if rooms  inc then it more window 

prlm :
Make coefficients unstable
Change coefficient values significantly with small data changes
Make feature interpretation unreliable
Reduce trust in the model

==============================================
pip install statsmodels  
from statsmodels.stats.outliers_influence import variance_inflation_factor 

detecting multicollineartiy using VIF :variance inflation factor

VIF (Variance Inflation Factor) measures how much the variance of a coefficient is increased because of multicollinearity.

VIF stands for Variance Inflation Factor.
It measures how strongly one independent variable is correlated with the other independent variables.
area  ----> bedroom , age 
bedrrom ---> area ,age 
age  ---> bedroom , area 

Remember:VIF does not compare a feature with the target (Price).
ex : 
VIF checks relationships like:

Area  <------> Bedrooms
Area  <------> Age
Bedrooms <------> Age

It does not check:
Area ------> Price

| VIF Value | Meaning                                                            |
| --------- | ------------------------------------------------------------------ |
| 1         | No correlation                                                     |
| 1 -5      | Acceptable                                                         |
| 5 - 10    | High correlation (investigate)                                     |
| >10       | Severe multicollinearity (consider removing or combining features) |
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from statsmodels.stats.outliers_influence import variance_inflation_factor 

# read data :

df = pd.read_csv("supervised machine learning/house_price.csv")
print(df.head())

# feature engineering :
X =df[['Area','Bedrooms','Age']]
y =df['Price']

# split data : 
X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,   # 80 % train 20 % test
    random_state=42
)

# create model :
model = LinearRegression()
model.fit(X_train,y_train)

#slope , intercept :
print("model slope :",model.coef_[0])
print("model intercept :",model.intercept_)

# prediction : 
y_pred = model.predict(X_test)
print("predicted value :",y_pred)

# comparison :   actual value and  predicted value 

comparison = pd.DataFrame({'Actual value':y_test.values,'predicted value':y_pred})
print(comparison)

coef = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
}
)
print(coef)
# evaluation :  mean square error
# VIF : variance inflation factor
# VIF
vif = pd.DataFrame()
vif["Feature"] = X.columns 
vif["VIF"] = [
    variance_inflation_factor(X.values, i)
    for i in range(X.shape[1])
]
print(vif)

importance = coef.copy()
importance["Absolute"] = importance["Coefficient"].abs()

print("\nFeature Importance")
print(
    importance.sort_values(
        by="Absolute",
        ascending=False
    )[["Feature", "Coefficient"]]
)
"""
The regression model predicts house prices reasonably well, but the VIF analysis reveals severe multicollinearity between Area and Bedrooms. Since these two features are highly correlated, their coefficient values are unstable and should not be used to judge feature importance. The Age feature has a low VIF, so its coefficient is more reliable. Before interpreting feature importance in Multiple Linear Regression, always check the VIF values.
"""
