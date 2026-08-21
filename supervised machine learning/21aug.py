"""
using  titanic  data set   -----> decision tree
draw the decision tree  -----> tree.import plot_tree

Decision Trees do not require feature scaling, so we normally do not use StandardScaler.
1. read csv 
2. check the  missing  value  , fill age  ----> with  median or  mean 
3. convert categorical column  ----> sex 
4. train test split
5. create the decision tree :
6. train model 
7. predict
8. accuracy
9. feature importance : using  function of  : feature_importances_
10. graph of  feature importance
11. visualize decision tree
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree

# read csv : 

df =pd.read_csv("supervised machine learning/Titanic-Dataset_2.csv")
# print(df.head())

# check missing value :
# print(df.isnull().sum())
df['Age']=df['Age'].fillna(df['Age'].median())

# convert categorical column :
df['Sex'] =df['Sex'].replace({'male':0,'female':1})

# choose the column : 
X =df[['Pclass','Sex','Age','SibSp','Parch','Fare']]
y=df['Survived']

#train test split :
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# choose the model : 

model = DecisionTreeClassifier(
    criterion='gini',
    max_depth=4,
    random_state=42
)
# train model :
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# accuracy score :
acc_score = accuracy_score(y_test, y_pred)
print(acc_score)

# feature importance :
feature_importances_ = model.feature_importances_
print("feature importance :", feature_importances_)

# graph of feature importance :

plt.bar(
    X.columns,
    feature_importances_
    
)
plt.xlabel('Features')
plt.ylabel('Importance')
plt.title('Feature importance')
plt.show()

# visualize decision tree :

plt.figure(figsize=(10,10))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=['0','1'],
    filled=True,
    rounded=True,
    fontsize=8
)
plt.title('Decision Tree')
plt.show()