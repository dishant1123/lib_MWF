
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
data = {
    "Age": [
        22, 45, 30, 52, 28,
        40, 35, 60, 25, 48,
        33, 55, 29, 42, 38,
        65, 24, 50, 31, 58
    ],

    "MonthlyCharges": [
        80, 60, 90, 50, 95,
        55, 85, 45, 100, 65,
        88, 52, 92, 58, 75,
        40, 105, 62, 87, 48
    ],

    "Tenure": [
        2, 36, 8, 60, 4,
        48, 10, 72, 3, 30,
        12, 55, 6, 40, 18,
        80, 2, 35, 9, 65
    ],

    "SupportCalls": [
        5, 1, 4, 0, 6,
        2, 5, 0, 7, 2,
        3, 1, 5, 2, 4,
        0, 8, 2, 5, 1
    ],

    "Churn": [
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0,
        0, 0, 1, 0, 1,
        0, 1, 0, 1, 0
    ]
}
df = pd.DataFrame(data)

X = df.drop("Churn", axis=1)
y = df["Churn"]

#TRAIN-TEST SPLIT :
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# CREATE GRADIENT BOOSTING MODEL
model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

# 10. TRAIN MODEL
model.fit(X_train, y_train)
print("\nModel Training Completed!")

# 11. PREDICTION
y_pred = model.predict(X_test)
print(y_pred)

# 12. PREDICT PROBABILITY
y_probability = model.predict_proba(X_test)
print("\nPrediction Probabilities:")
print(y_probability)

# 13. ACCURACY
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:")
print(accuracy * 100, "%")

# 14. CONFUSION MATRIX
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# 15. DISPLAY CONFUSION MATRIX

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Not Churn", "Churn"]
)
disp.plot()
plt.title("Gradient Boosting - Confusion Matrix")
plt.show()

# 16. CLASSIFICATION REPORT
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Not Churn", "Churn"]
    )
)
# 17. FEATURE IMPORTANCE

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print("\nFeature Importance:")
print(
    feature_importance.sort_values(
        by="Importance",
        ascending=False
    )
)

# 18. FEATURE IMPORTANCE VISUALIZATION
plt.bar(
    feature_importance["Feature"],
    feature_importance["Importance"]
)
plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Feature Importance - Gradient Boosting")
plt.xticks(rotation=45)
plt.show()

# 19. PREDICT A NEW CUSTOMER

new_customer = [[
    25,     # Age
    100,    # MonthlyCharges
    3,      # Tenure
    7       # SupportCalls
]]
new_prediction = model.predict(new_customer)
print("\nNew Customer Prediction:")
if new_prediction[0] == 1:
    print("Customer is likely to CHURN")
else:
    print("Customer is likely to NOT CHURN")

# 20. PREDICT PROBABILITY FOR NEW CUSTOMER
new_probability = model.predict_proba(new_customer)
print("\nProbability:")
print("Not Churn:", new_probability[0][0])
print("Churn:", new_probability[0][1])