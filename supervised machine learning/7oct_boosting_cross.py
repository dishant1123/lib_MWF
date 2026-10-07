"""
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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)
print("\nModel Training Completed!")


y_pred = model.predict(X_test)
print(y_pred)


y_probability = model.predict_proba(X_test)
print("\nPrediction Probabilities:")
print(y_probability)

accuracy = accuracy_score(y_test, y_pred)
print(accuracy * 100, "%")


cm = confusion_matrix(y_test, y_pred)
print(cm)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Not Churn", "Churn"]
)

disp.plot()
plt.title("Gradient Boosting - Confusion Matrix")
plt.show()

print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Not Churn", "Churn"]
    )
)
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

plt.bar(
    feature_importance["Feature"],
    feature_importance["Importance"]
)
plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Feature Importance - Gradient Boosting")
plt.xticks(rotation=45)
plt.show()

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

new_probability = model.predict_proba(new_customer)
print("Not Churn:", new_probability[0][0])
print("Churn:", new_probability[0][1])

"""
# cross validation  , pipeline :
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import (
    StratifiedKFold,
    cross_val_score
)
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

data = load_breast_cancer()

X = data.data
y = data.target

# 3. CREATE MODEL PIPELINE
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(
        max_iter=1000
    ))
])

# 4. CREATE STRATIFIED K-FOLD
skf = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
# 5. CROSS VALIDATION
scores = cross_val_score(
    model,
    X,
    y,
    cv=skf,
    scoring="accuracy")
# 6. DISPLAY FOLD SCORES
print("\nCross Validation Scores:")
for i, score in enumerate(scores, start=1):
    print(
        f"Fold {i}: {score:.4f}"
    )

# 7. MEAN SCORE
mean_score = scores.mean()
print("\nMean CV Accuracy:")
print(f"{mean_score:.4f}")

# 8. STANDARD DEVIATION
std_score = scores.std()
print("\nStandard Deviation:")
print(f"{std_score:.4f}")

# 9. MINIMUM AND MAXIMUM SCORE
print("\nMinimum CV Score:")
print(f"{scores.min():.4f}")
print("\nMaximum CV Score:")
print(f"{scores.max():.4f}")

"""We applied 5-Fold Stratified Cross Validation to evaluate the Logistic Regression model on the Breast Cancer dataset. The model achieved an average cross-validation accuracy of approximately 97.37%. The accuracy across the five folds remained relatively consistent, with a minimum of approximately 95.61% and a maximum of 98.25%. The relatively low standard deviation indicates that the model's performance does not vary greatly between folds. Therefore, cross-validation provides a more reliable estimate of model performance than relying on a single train-test split.
"""