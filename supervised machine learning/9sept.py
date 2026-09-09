
"""
step :1 read _csv  ---> breast cancer data
step :2 check class distribution
step :3 train-test split
step :4 feature scaling
step :5 create logistic regression model
step :6 train model
step :7 prediction , probability
step :8 accuracy ,precision ,recall ,f1 score
step :9 confusion matrix,classification report
step 10 : plot confusion matrix
step 11 : roc curve
step 12 : auc score
step 13 : precision-recall curve
step 14 : summary
"""

#======================
# cross validation  : 
#======================
"""
step :1 read _csv  ---> breast cancer data
step :2 create the pipline

from sklearn.pipeline import Pipeline
from sklearn.model_selection import (
    StratifiedKFold,
    cross_val_score
)

step :3 create the stratified k fold
step :4 create the cross validation score
step :5 display fold scores -----> loop  
step :6 mean,std ,min,max score  
step :7 conclusion
"""

import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report,roc_curve,auc,precision_recall_curve,precision_score,recall_score,f1_score,accuracy_score

from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

X= data.data 
y= data.target
print("X shape :",X.shape)
print("y shape :",y.shape)

#check  class distribution :

unique,counts = np.unique(y,return_counts=True)
for  class_value,count in zip(unique,counts):
    print(
        data.target_names[class_value],
        count
    )
# spilt  : 

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.3,   # 80 % train 20 % test  # train_size =.80 
    random_state=42
)

# scale data :

scaler = StandardScaler()
x_train_scale = scaler.fit_transform(X_train)
x_test_scale = scaler.transform(X_test)

# create model : 
model = LogisticRegression(max_iter=100)
model.fit(x_train_scale,y_train)

#  predict : 
y_pred = model.predict(x_test_scale)
prob = model.predict_proba(x_test_scale) 

# accuracy score :
accuracy = accuracy_score(y_test,y_pred)
print("accuracy :",accuracy)

# precision score :
precision = precision_score(y_test,y_pred)
print("precision :",precision)

# recall score :
recall = recall_score(y_test,y_pred)
print("recall :",recall)

# f1 score :
f1 = f1_score(y_test,y_pred)
print("f1 score :",f1)

# classification report :
classification_report = classification_report(y_test,y_pred)
print(classification_report)

# confusion  matrix : 
cm = confusion_matrix(y_test,y_pred)
print(cm)

# plot confusion matrix :

plt.figure(figsize=(8,8))
plt.imshow(cm,interpolation='nearest')
plt.title("Confusion matrix")
plt.colorbar()
tick_marks = np.arange(len(data.target_names))
plt.xticks(tick_marks, data.target_names,rotation=90)
plt.yticks(tick_marks, data.target_names)
plt.ylabel("True label")
plt.xlabel("Predicted label")
plt.show()

# roc_score : 
tpr,fpr,thresholds = roc_curve(y_test,
                               prob[:,1])

# auc score :
# precision-recall score:

# plot roc curve :

plt.figure(figsize=(8,8))
plt.plot(fpr,tpr)
plt.plot([0,1],[0,1],'r--')
plt.xlim([0,1])
plt.ylim([0,1])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Receiver operating characteristic")
plt.legend(["ROC curve","Random guess"])
plt.show()
# https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?utm_source=chatgpt.com