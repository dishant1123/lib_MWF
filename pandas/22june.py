import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
1. outlier detection  : 
"""

df = pd.DataFrame({
    'days' :[1,2,3,4,5,6,7,8,9,10], 
    "sales" :[100,200,250,350,170,300,400,500,600,10000]  # 318.89 1031.89 593 
})

print(df)

# box plot  : 
"""plt.boxplot(df['sales'])
plt.xlabel('days')
plt.ylabel('sales')
plt.title('sales')
plt.show()
"""

# outlier detection : IQR ,Z-score   : IQR = q3 -q1 

q1 = df['sales'].quantile(0.25)
q3 = df['sales'].quantile(0.75)  

IQR = q3 - q1
# print("IQR :",IQR)

upper_limit = q3 +1.5*IQR   #   263*1.5
lower_limit = q1 -1.5*IQR   #   -263*1.5

print("upper limit :",upper_limit)
print("lower limit :",lower_limit)

# outlier = df[(df['sales']<lower_limit) | (df['sales']>upper_limit)]
# print(outlier)


# z-score :
"""from scipy.stats import zscore

df['z_score'] = zscore(df['sales'])
outlier = df[df['z_score'].abs() > 2.5]
print(outlier)
"""

# capping outliers : depend upon of the upper and lower limit  for IQR : 

df['sales'] = df['sales'].clip(upper = upper_limit)
print(df)


# next : 2 outlier,convert,loc,iloc: