import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
"""
1. same  step till  accuracy score 
2. forward propagation : print  the w1 ,w2 ,b1,b2 
    take  : sample  = x_test[0:1]
            hidden  layer  
            activation function
            hidden layer output 
            activation function : sigmoid
3. graph : 

"""

df = pd.read_csv("Deep learning/purchase.csv")

# feature engineering
X=df[['Age','Monthly_Income']]
y=df['Purchase']

# split  data  :
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# scaler :
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# model  : 
model = MLPClassifier(
    hidden_layer_sizes=(3,),
    max_iter=1000,
    activation='relu',
    solver='adam'
)

# fit  model :
model.fit(X_train, y_train)

# predict :
y_predict =model.predict(X_test)
print("Prediction :", y_predict)

# accuracy :
print("Accuracy :", accuracy_score(y_test, y_predict))

# w1 ,w2 ,b1 ,b2 :
print("W1 :",model.coefs_[0])
print("W2 :",model.coefs_[1])
print("B1 :",model.intercepts_[0])
print("B2 :",model.intercepts_[1])

#forward propagation :

sample = X_test[0 :1]

# hidden  layer  :
hidden_layer = np.dot(sample, model.coefs_[0]) + model.intercepts_[0]
# x1w1 + x2w2 +b1 

# activation function :
activation_function  = np.max(0,hidden_layer)

# output  layer :
output_layer = np.dot(activation_function, model.coefs_[1]) + model.intercepts_[1]

print("Hidden layer :", hidden_layer)
print("Activation function :", activation_function)
print("Output layer :", output_layer)

# graph :

activations = np.concatenate([
    sample.flatten(),
    hidden_layer.flatten(),
    output_layer.flatten()
]) 

labels = [
    "Age",
    "Monthly_Income",
    "hidden layer",
    "Activation function",
    "Purchase"
]

plt.figure(figsize=(8,5))
plt.bar(activations,labels)
plt.xlabel("Activations")
plt.ylabel("Features")
plt.title("Activations vs Features")
plt.show()