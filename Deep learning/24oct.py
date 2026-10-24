import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import load_breast_cancer 
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten,batchnormalization
from tensorflow.keras.activations import relu
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.regularizers import l1, l2

data =load_breast_cancer()

X=data.data
y=data.target

#split : 
X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y,
                                                    test_size=0.2, 
                                                    random_state=42)

#scaler :
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# build model : 
tf.keras.set_random_seed(42)

build_model = Sequential([
    input(shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')])
    
    
summary = build_model.summary()
print(summary)
build_model.compile(optimizer=Adam,
                        batch_size=32,
                        loss='binary_crossentropy',
                        metrics=['accuracy']),
    
build_model.fit(
        X_train,
        y_train,
        epochs=100,
        validation_split=0.2,
        callbacks=[
            EarlyStopping(monitor='val_loss', patience=10)
        ]
)
  
# l1 , l2 : 
build_model_l1 = Sequential([
    input(shape=(X_train.shape[1],)),
    Dense(32, activation='relu', kernel_regularizer=l1(0.01)),
    Dense(16, activation='relu', kernel_regularizer=l1(0.01)),
    Dense(1, activation='sigmoid')])

         
# predict:
y_pred = build_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# probability:
y_pred_proba = build_model.predict_proba(X_test)
print("probability:", y_pred_proba)

