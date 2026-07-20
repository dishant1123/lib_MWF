import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
"""
df=pd.DataFrame({
    'age':[21,25,30,35,39],
    'salary':[25000,30000,35000,40000,100000]
})
"""
"""
age  : 
salary : 
"""
# KNN , k-means ,decision tree , random forest  

"""scaler = StandardScaler()
x_scaled = scaler.fit_transform(df)
result =pd.DataFrame(x_scaled,columns=df.columns)
# print(result)
"""
# convert : 0,1 maxmin scaler :  x -min / max-min  

"""scaler1 =MinMaxScaler()
x_scaled1 = scaler1.fit_transform(df)
result1 =pd.DataFrame(x_scaled1,columns=df.columns)
print(result1)
"""

df = pd.read_csv("supervised machine learning\customer_purchase_dataset.csv")
print(df)


"""realtion =df.corr(numeric_only=True)

sns.heatmap(data=realtion,annot=True,cmap='YlGnBu')
plt.show()
"""

# Recursive Feature Elimination : 