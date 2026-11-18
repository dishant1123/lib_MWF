import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Input, Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

"""
STEP 1: LOAD DATASET
STEP 2: CHECK MISSING VALUES
STEP 3: SELECT INPUT AND OUTPUT
STEP 4: TRAIN TEST SPLIT
STEP 5: FEATURE SCALING

STEP 6: CREATE SEQUENTIAL MODEL -----> API / SEQ  -----> dense layer ,activation  ----> relu, softmax, sigmoid  -----> output layer 
STEP 7: MODEL SUMMARY -----> 
STEP 8: COMPILE MODEL ------> optimizer, loss, metrics
STEP 9: TRAIN MODEL  ------> model.fit -----> x,y,batchsize , validation split, epochs
STEP 10: EVALUATE MODEL ----> model.evaluate
STEP 11: PREDICTION
STEP 12: ACCURACY SCORE
STEP 13: CLASSIFICATION REPORT
STEP 14: CONFUSION MATRIX

STEP 15: TRAINING AND VALIDATION ACCURACY
STEP 16: TRAINING AND VALIDATION LOSS

STEP 17: PREDICT NEW CUSTOMER
"""

# read :
df= pd.read_csv("Deep learning/bank.csv",sep=";")

# features selection  : 
X=df[['age','campaign','previous']]
y=df['y'].map({'no':0,'yes':1})

# train test split :
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y, 
                                                    test_size=0.2, 
                                                    random_state=42)

# feature scaling :
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test) 

# model  :  
model = Sequential([
    Input(shape=(3,)),
    Dense(16, activation='relu'),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid'),
])

# summary  : 
model.summary()

# compile  :
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# fit  :
history=model.fit(X_train, 
          y_train, 
          epochs=20, 
          validation_split=0.2, # during training not update the  weight of the model
          verbose=1)

# evaluate  :
loss,accruacy = model.evaluate(X_test,
                               y_test,
                               verbose=0)

print("test loss : ",loss)
print("test accuracy : ",accruacy) 
print("accuracy  in percentage : ",accruacy*100)

# predict  :
y_probabilities =model.predict(X_test)
y_pred =(y_probabilities >=0.5).astype(int).ravel()

# accuracy score  :
print("accuracy score : ",accuracy_score(y_test,y_pred))

# classification report  :
print("classification report : \n")
print(classification_report(y_test,y_pred))

# confusion  matrix : 
print("confusion matrix : \n")
print(confusion_matrix(y_test,y_pred))

#training and  validation accuracy : 
plt.figure(figsize=(10,5))

plt.plot(
    history.history['accuracy'],
    label='training accuracy'   
)

plt.plot(
    history.history['val_accuracy'],
    label='validation accuracy'
)
plt.title('training and validation accuracy')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend()
plt.grid()
plt.show()

#training and  validation loss :
plt.figure(figsize=(10,5))

plt.plot(
    history.history['loss'],
    label='training loss'   
)

plt.plot(
    history.history['val_loss'],
    label='validation loss'
)
plt.title('training and validation loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.grid()
plt.show()

#new customer predict :  -----> age  ,campaign, previous  -----> scaled  ----->predict  ----> prob. > 0.5  

