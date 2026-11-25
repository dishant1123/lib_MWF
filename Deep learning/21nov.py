import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Concatenate
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score

"""
1. load the  dataset  
2. duplicated row remove  
3. select input features : half feature take x1 and  half feature take x2 
            x1 = []  4 
            x2= [] 5  
            y = [g2 ,g3 ]
4. encode  cat data with get_dummies  : x2 ----> get_dummies() ,drop (True)
5. split the data into train and test  : x1 x2 

    x1_train, x2_train  = train_test(
        x1,x2,y,test_size = 0.2
    )
6. scale the data :  
    scale1 = stand 
    scale2 =stand
7. create  API : take the  two input   

    input1 = Input(shape = (4,),name=)
    input2 = Input(shape = (5,),name=)
    
    branch1 = dense(32,activation = 'relu')(input1)
             dense(16,activation = 'relu')(input1)
    branch2 = dense(32,activation = 'relu')(input2)
             dense(16,activation = 'relu')(input2)
             
    combine = concatenate([branch1,branch2])
    hidden_layer =dense(32,activation = 'relu')(combine) 
    
    output1 = dense(1,activation = 'linear')(hidden_layer)
    output2 = dense(1,activation = 'linear')(hidden_layer)
    
Model  = model (input 1 inut 1 , outpuet1 output2)


8. branch1 and branch2 
9. concatenate the two branch
10.hidden 
11.output 1 , output 2 
12. model ,summary ,complie , fit , evaluate , predict
"""
