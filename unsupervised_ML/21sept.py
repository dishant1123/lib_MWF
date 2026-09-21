# K-means clustering
"""
type  unsupervised ML : 

1. clustering : 
    1. k-means clustering
    2.hierarchical clustering
    3.DBSCAN
2. dimensionality reduction :
    1. PCA
    2. t-SNE
    3. UMAP
3. association rule learning   

----> real life example  : customer segmentation,anomaly detection , feedback prediction


clustering : group similar data together
ex : 

customer    income    spending   
A           20        30 
B           22        35 
C           80        90
D           85        90
 
step :1 k-means   -----> k value   ----> number of cluster/ group  
step :2 calculate distance between each customer and each cluster
step :3 create  clsuter 

cluster A :  ------> budget fix ,small 
    customer A
    customer B
cluster B :  ------> premiun customer/ high budget 
    customer C
    customer D
    
K-means : its divides data  into  K clusters.  

centroid : the  center of the cluster.

(2,3)
(4,5)
(6,7)

centroid :  -----> x = 2+4+6 /3 =4 
            -----> y = 3+5+7 /3 =5
centroid : ------> (4,5)

ex :1  
point         X        y 
p1            1        1 
p2            2        1
p3            4        3 
p4            8        8 
p5            9        8 
p6            8        9

k=2

intial centroid : c1 = (1,1) , c2 = (8,8)

cluster : 1 p1 p2 p3 
update centroid : (1+2+4)/3 = 2.33 
                  (1+1+3)/3 = 1.67
                 = 2.33 ,1.67 
                  
cluster : 2 p4 p5 p6
update centroid : (8+9+8)/3 = 8.33
                  (8+8+9)/3 = 8.33
                 = 8.33 ,8.33 

-----> distance  between centroid and point

2 method  : 
1.  euclidean distance 
    squreroot  (x2 -x1)^2  + (y2 -y1)^2

2.  manhattan distance
    (x2 -x1)^2  + (y2 -y1)^2

k value  :  random  
choosing  best k value  : 
    1. elbow method 
    2. WCSS method ----> within cluster sum of squares
    
advantages :
1. easy  to understand
2. fast for  large data
3. scalable : can handle  thousands of dataset 
4. eiffcient  
5.use : customer segmentation , market anaysis , document clustering

disadvantages :
1. k value 
2. sensitive to initial centroid : different k value  will give different result/ centroid
3. irregular clsuter shape   
4. numerical data preference
"""

# ex :1 

from sklearn.cluster import KMeans 
import pandas as pd


data ={
    "income" : [10,12,15,50,60,75]
}
df =pd.DataFrame(data)
k_means =KMeans(n_clusters=2,random_state=42)

df['cluster']=k_means.fit_predict(df)

print(df)
print("centroid :",k_means.cluster_centers_)  # centroid 