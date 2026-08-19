import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

"""df =pd.DataFrame(data.data, columns=data.feature_names)
print(df.info())
"""
X=pd.DataFrame(data.data, columns=data.feature_names)
y=pd.Series(data.target)

# print(X.head())
# print(y.head())

# split :
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.3, 
    random_state=42)

# scaler :

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train, y_train)
X_test = scaler.transform(X_test)

# model  : 
"""
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_predict =knn.predict(X_test)
"""
# accuracy  score :
"""acc_score =accuracy_score(y_test,y_predict)
print(acc_score)
"""
# classfication report , confusion matrix 

"""for i in range(1,6):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    y_predict =knn.predict(X_test)
    acc_score =accuracy_score(y_test,y_predict)
    print(acc_score)
"""

# elbow method : 

k_values =range(1,11)
accrucies =[] 

for  i in k_values:  # 1,11
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    y_predict=knn.predict(X_test)
    acc_score=accuracy_score(y_test,y_predict)
    accrucies.append(acc_score)
    
plt.plot(k_values,accrucies)
plt.xlabel('k values')
plt.ylabel('accuracy')
plt.title('Accuracy score vs k values')
plt.show()

# cross validation :
# GridSearchCV
