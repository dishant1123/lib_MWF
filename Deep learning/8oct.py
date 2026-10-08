import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neural_network import MLPClassifier

df=pd.read_csv("Deep learning/mlp_student_performance.csv")
print(df.head())

# feature engineering
X=df[['Study_Hours','Attendance','Assignments']]
y=df['Result']

# split  data  : 
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.3, 
    random_state=42)

# scaler : 
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# model : 
model = MLPClassifier(
    hidden_layer_sizes=(5,3), 
    max_iter=1000,
    activation='relu',  # activation function 
    solver='adam'  # loss 
)

# fit  model : 
model.fit(X_train, y_train)

# predict : 
y_predict =model.predict(X_test)

# accuracy :
accuracy =accuracy_score(y_test, y_predict)
print("Accuracy" , accuracy)

# classification report :
classification  = classification_report(y_test, y_predict)
print("classification report" , classification)

# new data  : 
new_data_df = pd.DataFrame({
    "Study_Hours" :[4.8],
    "Attendance" :[77],
    "Assignments" :[57]
})

new_data = scaler.transform(new_data_df)

predictions_new_data = model.predict(new_data)

print("Predictions" , predictions_new_data[0])
