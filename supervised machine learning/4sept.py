import  pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_auc_score,f1_score,precision_score,recall_score

df = pd.read_csv("supervised machine learning/Churn_Modelling (1).csv")
print(df.head())

# missing value  : 
print(df.isnull().sum())

# male : 1 female : 0 
df['Gender']=df['Gender'].map({'Male':1,'Female':0})

# feature selection :

X=df[['CreditScore','Gender','Age',"Tenure","EstimatedSalary",'Balance','NumOfProducts','HasCrCard','IsActiveMember']]
y=df['Exited']

# split data :
X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# model : 

model =XGBClassifier(n_estimators=100,
                     max_depth=5,
                     learning_rate=0.1,
                     random_state=42)

model.fit(X_train,y_train)

# predict :
y_pred = model.predict(X_test)

# accuracy :
accuracy = accuracy_score(y_test,y_pred)
print("accuracy :",accuracy*100)

# confusion matrix :
conf_matrix = confusion_matrix(y_test,y_pred)
print(conf_matrix)

# classification report :
class_report = classification_report(y_test,y_pred)
print(class_report)

# feature importance :
feature_importance = model.feature_importances_
data =pd.DataFrame({'feature':X.columns,'importance':feature_importance})
data.sort_values(by='importance',ascending=False)
print(data)

"""
[[1530   63]
 [ 224  183]]


Tp => 1530 Actual = Positive, Prediction = Positive.
Fn => 63  Actual = Positive, Prediction = Negative
Fp => 224 Actual = Negative, Prediction = Positive.
Tn => 183 Negative, Prediction = Negative.
"""

# probability :

# prob = model.predict_proba(X_test)


# print roc ,auc ,curve : 

# conclusion : 

