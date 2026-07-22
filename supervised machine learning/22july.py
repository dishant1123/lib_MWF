"""
==>RFE (Recursive Feature Elimination):It repeatedly removes the least important feature until only the desired number remain.

1.regression :
2.when we use regression  : number and continuous value.
3.simple regression  : y =mx+c  
				y=predicted value 
				x=independent variable 
				m=slope :The slope tells us how much the predicted value changes when the input increases by one unit.
				c=intercept (value of y when x is 0)
4. relationship : positive ,negative 
5.cost function : how far the model's prediction are from actual value.
	ex:actual cost =70000
	   modelpredict =67000
	   loss =3000	
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

# read _csv :

"""df =pd.read_csv("supervised machine learning\customer_purchase_dataset.csv")
# print(df)

# IQR : 
Q1 =df['Salary'].quantile(0.25)
Q3 =df['Salary'].quantile(0.75)

IQR =Q3-Q1

# upper and lower bound :
upper=Q3 +1.5*IQR
lower=Q1-1.5*IQR

df =df[(df['Salary']>lower) & (df['Salary']<upper)]
print(df)

# features selection  : 
X=df[['Age','Experience','Purchased']]
y=df[['Salary']]

# scale : 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# model :
model = LogisticRegression()
selector =RFE(model,n_features_to_select=1)
model.fit(X_scaled,y)

#select features :
print(selector.fit(X_scaled,y).support_)
"""