import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score

# load data  set :

df = pd.read_csv("supervised machine learning/Titanic-Dataset_2.csv")
print(df.head())

# info()
"""print(df.info())
print(df.describe())
print(df.isnull().sum())
"""

# fill the missing value :

df['Age'] =df['Age'].fillna(df['Age'].median())
df['Embarked'] =df['Embarked'].fillna(df['Embarked'].mode()[0])
# print(df.isnull().sum())

# sex ----> using  replace or  map  
df['Sex'] =df['Sex'].replace({'male':0,'female':1})
# df['Sex'] =df['Sex'].map({'male':0,'female':1})

# features selection :

X =df[
    ['Pclass',
     'Sex',
     'Age',
     'SibSp',
     'Parch',
     'Fare',
     ]
]
y=df['Survived']

# split data set :
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y, 
                                                    test_size=0.3, 
                                                    random_state=42)

# create model :
model = LogisticRegression(max_iter=100)
model.fit(X_train, y_train)

# prediction  :
y_pred = model.predict(X_test)
print("prediction :", y_pred)

# probability :
prob = model.predict_proba(X_test)
print("probability :", prob)

# accuracy :
accuracy = accuracy_score(y_test, y_pred)
print("accuracy :", accuracy*100)

