
# hyperparameter turning  and  model  improvement :
# using  load_breast_cancer() : from  sklearn 

"""
1.load the dataset 
2.feature selection   
3.split the data  
4.scale  
5.create  the basic  model  
6.compile  , fit , evaluate 
7.compare the  different configuration  
    a. check the  different  batch size  
    b. epoch 
    c. optimizer : sgd ,rmsprop,adam 
    d. LR 
    e. weight_intialization  : he_normal,glorot_uniform 
        kernel_intializer 
8.automated hyperparameter tuning : using  function  
9.create turner  : using kt.randomsearch() 
10.fit the  turner : turner.search() 
11. print  the best_model  : turner.get_best_model() ,turner.get_best_hyperparameters()
12.evaluate 
13.plot 

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tensorflow as tf
import keras_tuner as kt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam, SGD, RMSprop
 
