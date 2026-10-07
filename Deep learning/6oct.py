"""
    1. read csv 
	2. condition  : marks > 50  1   ----> else 0  -----> np.where 
	3. input  and target  -----> x  ---> hrs .value  y ---->result.value 
	4. weight and bias  ----> wieghts ---> np.zeros(x.shape[1]),bais ,learning_rate,epochs
	5. function  :  value > 0  ---->return 1 else ----> 0
	6. training :  for loop  ---> taken nested  loop  ---> input  , output ,weight_sum, prediction,error. 								update_weight, total_error 
	7. prediction :
	8. Accuracy
 
 
 z = x1w1 + x2w2 + b 
"""
import pandas as pd 
import  numpy as np 


df = pd.read_csv("Deep learning/study_marks.csv")
print(df.head())
   
# using  np.where using  marks > 50 1 else 0 

df['result']=np.where(df['Marks'] > 50, 1, 0)
print(df)

# input and target

X = df[['Study_Hours']].values
y= df['result'].values

# weight and bais : 
weights = np.zeros(X.shape[1])
bias = 1
learning_rate = 0.01
epochs =10

# function  :  value > 0  ---->return 1 else ----> 0
def step_function(value):
    if value > 0:
        return 1 
    else :
        return 0
    
# training  : 
for i in range(epochs):
    total_error =0 
    for j  in range(len(X)):
        input = X[j]
        output = y[j] 
        
        weight_sum =  np.dot(input , weights) + bias
        prediction  = step_function(weight_sum)
        error = prediction - output
        weights = weights + learning_rate * error * input
        
        bias = bias + learning_rate * error
        
        total_error = total_error + error 
        
        print(
            "epochs" , epochs+1,
            "weight" , weights,
            "bias" , bias
        )
        
# prediction  : 
predictions  = [] 
for i in range(len(X)):
    weight_sum   = np.dot(X[i] , weights) + bias
    prediction  = step_function(weight_sum)
    predictions.append(prediction)

# Accuracy : 

correct = np.sum(predictions == y)
total = len(predictions)
accuracy = correct/total
print("Accuracy" , accuracy)