"""
SVM  : practical example 

"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

data = {
    "Age": [
        22, 25, 28, 30, 32,
        35, 38, 40, 42, 45,
        48, 50, 52, 55, 58
    ],
    "Salary": [
        25000, 30000, 35000, 40000, 45000,
        50000, 55000, 60000, 65000, 70000,
       75000, 80000, 85000, 90000, 95000
    ],
    "Purchased": [
        0, 0, 0, 0, 0,
        0, 1, 1, 1, 1,
        1, 1, 1, 1, 1
    ]
}

df = pd.DataFrame(data)
print(df)

X=df[['Age', 'Salary']]
y=df['Purchased']

# split :
X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size=0.3, 
                                                    random_state=42)

# scale :

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#model : 

svc = SVC(kernel='linear')

# model fit :
svc.fit(X_train, y_train) 

# model predict :
y_pred = svc.predict(X_test)

# model accuracy :
accuracy = accuracy_score(y_test, y_pred)
print(accuracy*100, "%")

# new data predict :
new_data = [[43,63450]]

new_scaler = StandardScaler()
new_data = new_scaler.fit_transform(new_data)

predict = svc.predict(new_data)
print("new  data predict : ", predict)
