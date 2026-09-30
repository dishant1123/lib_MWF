"""
1. read csv ----> mall customer 
2. feature selection  
3. scale
4. apply PCA ,fit_tranform 
5. explain the variance 
6. create the dataframe  of the  pca 
7. plot  pca 1 ,pca 2 
8 . remaining stpes  are same as previous file
"""

import  pandas as pd 
import numpy as np 
from sklearn.cluster  import DBSCAN
from sklearn.decomposition import PCA 
from sklearn.preprocessing import StandardScaler 
import matplotlib.pyplot as plt


df = pd.read_csv("unsupervised_ML/Mall_Customers.csv")
# print(df.head())

# feature selection:
X=df[['Age','Annual Income (k$)','Spending Score (1-100)']]

# sclae the data :

scaler = StandardScaler()
x_scaled = scaler.fit_transform(X)

# apply pca :
pca = PCA(n_components=2)
X_pca = pca.fit_transform(x_scaled)

# explain the variance :

pca_variance = pca.explained_variance_ratio_
sum_explained_variance = np.sum(pca_variance)
print(sum_explained_variance)

# datafram  of the  pca : 

df_pca = pd.DataFrame(
    X_pca,
    columns=['PCA1', 'PCA2']
    
)
print(df_pca) 

# plot pca 1 ,pca 2 :

plt.figure(figsize=(8, 5))
plt.scatter(
    df_pca['PCA1'],
    df_pca['PCA2'],
    c=df['Spending Score (1-100)'],
    s=100
)
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.title('PCA')
plt.show()


