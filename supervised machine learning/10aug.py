"""
TTS  : python 8-9 , 9-10 SQL ,10-11 excel stats 3.30 - 4.30 
MWF  : 4-5.30 python ---> function 6-7 numpy 2 7-8 matplotlib  
"""
# liner_model import logistic regression 

# read , x ,y  ,split  , model = logistic regression  model.fit  , model.predict (x) 
# pro
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("supervised machine learning/student_pass.csv")

print(df.head())

# Features and target
X = df[['StudyHours']]
y = df['Pass']

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Predictions
predictions = model.predict(X)

# Probability predictions
probabilities = model.predict_proba(X)

print("\nPredicted Class")
print(predictions)

print("\nProbability")
print(probabilities)

# Accuracy
accuracy = model.score(X, y)
print("\nAccuracy :", accuracy)

new_student = [[4.5]]
prediction = model.predict(new_student)
probability = model.predict_proba(new_student)
print("Prediction :", prediction)
print("Probability :", probability)

import numpy as np
import matplotlib.pyplot as plt
"""
x = np.linspace(-10, 10, 200)  # start -10  end 10  step 200  ----> stop -start /step-1

y = 1 / (1 + np.exp(-x))

plt.figure(figsize=(8,5))
plt.plot(x, y)

plt.title("Sigmoid Function")
plt.xlabel("z")
plt.ylabel("Probability")
plt.grid(True)

plt.show()
"""
import matplotlib.pyplot as plt
import numpy as np

plt.scatter(X, y, color='blue', label='Actual Data')

X_test = np.linspace(X.min(), X.max(), 200).reshape(-1, 1)
y_prob = model.predict_proba(X_test)[:, 1]

plt.plot(X_test, y_prob, color='red', linewidth=2)

plt.axhline(y=0.5, color='green', linestyle='--', label='Threshold = 0.5')

plt.xlabel("Study Hours")
plt.ylabel("Probability of Passing")
plt.title("Logistic Regression with Sigmoid Curve")
plt.legend()

plt.show()
