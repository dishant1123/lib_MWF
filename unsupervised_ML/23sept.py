import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# read data :
df = pd.read_csv("unsupervised_ML/Wholesale customers data.csv")

# understand data :

print(df.info())
print(df.isna().sum())

# 