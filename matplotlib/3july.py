"""
# seaborn  : less code ,statis graph , style 

1.histplot : maths ==> bins =5 
2.KDE plot : show  probabilties distribution 
3.displot  : combine  hist + kde 
4.box plot : find  outlier 
5.Violin Plot :Shows distribution + boxplot together.
6.countplot : count the  categories 
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = {
    "Student":["A","B","C","D","E","F","G","H","I","J"],
    "Gender":["Female","Female","Female","Male","Male","Female","Female","Female","Male","Female"],
    "Math":[78,85,90,65,72,88,95,70,80,92],
    "Science":[82,89,91,68,74,90,96,73,81,94],
    "English":[75,80,88,60,70,86,92,72,79,90],
    "Attendance":[90,95,98,80,85,97,99,88,91,96]
}

df = pd.DataFrame(data)
print(df)

# histplot :
"""sns.histplot(data=df, x="Math", bins=5,hue="Gender", multiple="stack")
plt.title("Distribution of Students")
plt.show()
"""

# kde plot :
"""sns.kdeplot(data=df['Science'], fill=True)
plt.title("Distribution of Students")
plt.show()
"""

# displot :
"""# sns.displot(data=df['English'],kde=True, fill=True)
sns.displot(data=df['English'],kind="ecdf")

plt.title("Distribution of Students")
plt.show()
"""

# boxplot :

"""sns.boxplot(data=df['English'])
plt.title("Distribution of Students")
plt.show()
"""

# violin plot :

"""sns.violinplot(data=df['English'])
plt.title("Distribution of Students")
plt.show()
"""
# count plot  : 

sns.countplot(data=df['Gender'] ,color="green")
plt.title("Distribution of Students for  gender wise")
plt.show()#
