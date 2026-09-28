import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
import numpy as np 
"""
step :1 read csv 
step :2 check the  null values,missing values , fill missing values
step :3 select features
step :4 create graph
step :5 scale the data
step :6 apply dbscan
step :7 display the cluster labels : df['cluster'].values
step :8 number of clusters
step :9 count the number of noise points
step :10 display the noise points
step :11 display each cluster
step :12 visualize dbscan clusters
step :13 highlight noise points
"""

"""
for selection  of the  eps   : k-distance graph 

1. import NearestNeighbors ----> give  the value of  n_neighbors 
2. fit the  model 
3. distance , indices
4.distance  ---> using np.sort() sorted 
"""

df = pd.read_csv("unsupervised_ML/customer.csv")

X = df[['Age','Annual_Income','Spending_Score']]

# graph  the data : 


plt.scatter(X['Age'],X['Spending_Score'],c="violet",s=100)
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.show()


# scale the data :

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X) 

# eps k distance graph

"""neighbours = NearestNeighbors(n_neighbors=3).fit(X_scaled)
distances, indices = neighbours.kneighbors(X_scaled)

print(distances,indices)
k_distance =distances[:,2]
k_distance = np.sort(k_distance)

plt.figure(figsize=(10,10))
plt.plot(k_distance)
plt.title("neighboring points")
plt.grid(True)
plt.show()
"""
# apply dbscan :
db =DBSCAN(eps=0.8,
           min_samples=5).fit(X_scaled) 

df['cluster'] =db.fit_predict(X_scaled)
print(df)

# display the cluster labels :
print(df['cluster'].values)
noise_points = df[df["cluster"] == -1]
print(noise_points)

# graph DBSCAN Clusters
plt.figure(figsize=(8, 5))
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=df["cluster"],
    s=100
)
plt.xlabel("Income (Scaled)")
plt.ylabel("Spending Score (Scaled)")
plt.title("DBSCAN Clustering")
plt.show()

# hightlight  Noise Points
plt.figure(figsize=(8, 5))
plt.scatter(
    X_scaled[df["cluster"] != -1, 0],
    X_scaled[df["cluster"] != -1, 1],
    c=df.loc[df["cluster"] != -1, "cluster"],
    s=100
)
# Plot noise points separately
plt.scatter(
    X_scaled[df["cluster"] == -1, 0],
    X_scaled[df["cluster"] == -1, 1],
    marker="x",
    s=150,
    label="Noise"
)
plt.xlabel("Income (Scaled)")
plt.ylabel("Spending Score (Scaled)")
plt.title("DBSCAN - Clusters and Noise")
plt.legend()
plt.show()


# hw : mall_customer.csv -------> kaggle dataset
