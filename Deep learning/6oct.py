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

# 
