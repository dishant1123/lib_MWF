# kmeans  using  train  test : 
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 1. Read Dataset
df = pd.read_csv("unsupervised_ML/customer.csv")

# 2. Select Features

X = df[[
    "Age",
    "Annual_Income",
    "Spending_Score"
]]

# 3. Train Test Split

X_train, X_test = train_test_split(
    X,
    test_size=0.20,
    random_state=42
)
print("Training:", X_train.shape)
print("Testing:", X_test.shape)

# 4. Standardization

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Create KMeans   : for choosing best  k-value then  use eblow method wcss method 
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# 6. Train Model
kmeans.fit(X_train_scaled)

# 7. Training Data Prediction
train_clusters = kmeans.predict(X_train_scaled)
print("\nTraining Clusters:")
print(train_clusters)

# 8. Test Data Prediction
test_clusters = kmeans.predict(X_test_scaled)
print("\nTest Clusters:")
print(test_clusters)

# 9. Show Test Result
test_result = X_test.copy()
test_result["Cluster"] = test_clusters
print("\nTest Result:")
print(test_result)

# 10. NEW CUSTOMER

new_customer = pd.DataFrame({
    "Age": [27],
    "Annual_Income": [32000],
    "Spending_Score": [85]
})

# Scale new customer
new_customer_scaled = scaler.transform(new_customer)

# Predict cluster
new_cluster = kmeans.predict(new_customer_scaled)
print("\nNew Customer:")
print(new_customer)
print(
    "New Customer belongs to Cluster:",
    new_cluster[0]
)

# 11. Centroids

print("\nCluster Centers:")
print(kmeans.cluster_centers_)


# k-means clustering graph
plt.scatter(
    X_train_scaled[:, 0],
    X_train_scaled[:, 1],
    c=train_clusters,
    s=50,
    cmap="viridis"
)
plt.title("K-Means Clustering")
plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.show()

silhouette_avg = silhouette_score(X_train_scaled,kmeans.labels_)
print("The average silhouette_score is :", silhouette_avg)
