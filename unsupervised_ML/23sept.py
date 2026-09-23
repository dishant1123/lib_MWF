import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# read data :
df = pd.read_csv("unsupervised_ML/Wholesale customers data.csv")

# understand data :

print(df.info())
print(df.isna().sum())

# drop  : channel ,region  :

X = df.drop(['Channel','Region'],axis=1)
# print(df.head())

#scale data :

scler = StandardScaler()
X= scler.fit_transform(X)

#elbow method :
"""
wcss=[] 

for i in range(1,11):
    kmeans = KMeans(n_clusters=i,random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),wcss)
plt.xlabel('k value')
plt.ylabel('WCSS')
plt.show()
"""

# k-means clustering :
k_means = KMeans(n_clusters=3,random_state=42)
k_means.fit(X)

#predict :
df['cluster']=k_means.predict(X)
print(df.tail(20))

#number of  customer for each cluster :
print(df['cluster'].value_counts())

# centroid :
centroid = k_means.cluster_centers_
print("centroid :",centroid)

