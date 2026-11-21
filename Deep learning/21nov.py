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
4. encode  cat data with get_dummies 
5. split the data into train and test
6. scale the data
7. create  API : take the  two input  
8. branch1 and branch2 
9. concatenate the two branch
10.hidden 
11.output 1 , output 2 
12. model ,summary ,complie , fit , evaluate , predict
"""
