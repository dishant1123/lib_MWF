
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
1.read csv ----> study_marks.csv
2.weight and bias intialize -----> with  0  , lr =0.001 , epochs =2000
3. calculate the gradient ---->  using for loop  
     forward propagation : w * X + b
     MSE = np.mean((y_pred - y) ** 2)
     gradients : dw = (2 / n) * np.sum(X * (y_pred - y))
                 db = (2 / n) * np.sum(y_pred - y)
     update weight and bias : w = w - learning_rate * dw
                              b = b - learning_rate * db
4. predict marks  : 4.7 
5.plot 

"""
# ex :1 

df =pd.read_csv("Deep learning/study_marks.csv")

X=df['Study_Hours'].values
y=df['Marks'].values

w=0.0 
b=0.0 
lr=0.001
epochs=1000
n=len(X)

history_loss = []
for i in range(epochs):
     # forward propagation
     y_pred = w * X + b
     
     # mse : 
     loss = np.mean((y_pred - y) ** 2)
     history_loss.append(loss)
     
     # calculate the gradient
     dw = (2 / n) * np.sum(X * (y_pred - y))
     db = (2 / n) * np.sum(y_pred - y)
     
     # update weight and bias
     w =w - lr* dw
     b = b - lr * db
     
     print(f"Epoch {i+1} loss : {loss}")

# final model : 
print(f"final model : w = {w} , b = {b}")

# predict marks
hours =4.7 
y_pred = w * hours + b
print(f"predict marks : {y_pred}")

# plot :
plt.plot(history_loss)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Gradient descent")
plt.show()

