import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# bar charts labels : 
"""
df= pd.read_csv("matplotlib\student.csv")

bar =plt.bar(df['name'],df['science'],color='blue',edgecolor='black',width=0.5)
plt.xlabel('name')
plt.ylabel('science')
plt.title("student's science marks")

for i in bar :
    plt.text(
        i.get_x() + i.get_width()/2,
        i.get_height() + 1,
        i.get_height(),
        ha='center',  # horizontal alignment
        fontsize=12,
        color='black'
    )

# plt.grid(True)
plt.legend(labels=['science'],loc='upper right')
plt.show()
"""

# group bar charts:

"""
df= pd.read_csv("matplotlib\student.csv")
print(df)

x =np.arange(len(df['name']))  # [0 to 7]
width =0.3 

plt.figure(figsize=(10,6))
bar1 = plt.bar(
    x-width,
    df['maths'],
    color='blue',
    edgecolor='black',
    width=width,
    label='math'
)
bar2 =plt.bar(
    x,
    df['eng'],
    color='red',
    edgecolor='black',
    width=width,
    label='eng'
)

bar3 =plt.bar(
    x+width,
    df['science'],
    color='green',
    edgecolor='black',
    width=width,
    label='science'
)

for  bars in [bar1,bar2,bar3] :
    for  i in bars :
        plt.text(
            i.get_x() + i.get_width()/2,
            i.get_height() + 1,
            i.get_height(),
            ha='center',  # horizontal alignment
            fontsize=12,
            color='black'
        )
plt.xlabel('name')
plt.xticks(x,df['name'])
plt.ylabel('marks')
plt.title("student's marks")
plt.grid(alpha=0.5)  # alpha : transparency
plt.legend(labels=['math','eng','science'],loc='upper right')
plt.ylim(0,105)
plt.show()
"""

# donut chart :

"""mobile =['nokia','samsung','apple','htc','motorola']
sales_in_qty = [10,200,90,40,30]
width = 0.7
plt.pie(sales_in_qty,labels=mobile,startangle=90,autopct='%1.2f%%',wedgeprops={'width':0.4})
plt.title("pie chart")
plt.show()
"""

# box plot : 
"""
df= pd.read_csv("matplotlib\student.csv")

plt.boxplot(df[['maths','science','eng']],labels=['maths','science','eng'])
plt.title("box plot")
plt.show()
"""

# subplot : 
df= pd.read_csv("matplotlib\student.csv")

plt.figure(figsize=(10,8))
plt.subplot(2,2,1)
plt.plot(df['maths'],color='red',marker='o',linestyle='-',linewidth=2)
plt.title("maths")

plt.subplot(2,2,2)
plt.bar(df['name'],df['science'],color='blue',edgecolor='black')
plt.title("science")

plt.subplot(2,2,3)
plt.hist(df['eng'],bins=4,color='blue',edgecolor='black')
plt.title("science")

plt.subplot(2,2,4)
plt.scatter(df['maths'],
            df['study_hrs'],
            color='red',
            marker='o',
            s=100)
plt.title("scatter")

plt.tight_layout()
plt.show()