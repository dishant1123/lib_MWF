"""
matplotlib :  pip install matplotlib 

what is  viszalization ??  -==> graphical  presentation  ===> graphs 

matplotlib vs seaborn : 

use matplotlib  : 
    a. simple graphs , statistics analysis  
        ex : plot (line), bar , scatter, histogram, boxplot, pie 
    b. to much code         
use seaborn : 
    a. heatmap 
    b. corelation analysis
    c. less code  ===> style  
    
matplotlib labels : 
    x axis : xlabel 
    y axis : ylabel
    title : title 
    grid : 
    figure size : (8,6)
    color , marker ,legend : 
    show()    
"""
import pandas as pd 
from matplotlib import pyplot as plt 

# csv file  : 

# 1. plot (line ) graph : 

df= pd.read_csv("matplotlib\student.csv")
"""
# print(df) 
   # linewidth = thickness of line
   
plt.figure(figsize=(8,6)) 
plt.plot(df['name'],df['maths'],color='red',marker='o',linestyle='-',linewidth=2)
plt.xlabel('name')
plt.ylabel('maths')
plt.title("student's maths marks")
plt.grid(True)
plt.legend(labels=['maths'],loc='upper right')
plt.show()
"""
# which  student  got  highest  maths  marks  and  lowest math marks ?  

# scatter plot :

"""plt.scatter(df['maths'],
            df['science'],
            df['study_hrs'],
            color='red',
            marker='o',
            s=100)

plt.xlabel('maths')
plt.ylabel('study_hrs')
plt.title("scatter plot")
plt.grid(True)
plt.legend(labels=['maths'],loc='upper left')
plt.show()
"""

# bar plot : 

plt.bar(df['name'],df['science'],color='blue',edgecolor='black')
plt.xlabel('name')
plt.ylabel('science')
plt.title("student's science marks")
# plt.grid(True)
plt.legend(labels=['science'],loc='upper right')
plt.show()

