"""
1.deepcopy  ,shallow copy  
2.indexing  
3.slicing
4.broadcasting 
"""
import  numpy as np
# deep copy  : new object  + original array  ===> no changes 
"""
arr =np.array([1,2,3])
arr2 = arr.copy()  # new object  + original array  ===> no changes

arr2[1] =90
print("original  array : ",arr)
print("edit array :",arr2)
"""

# shallow copy  : new object  + original array  ===> changes

"""arr =np.array([1,2,3])

arr2 = arr.view()
arr2[1] =900 
print("original  array : ",arr)
print("edit array :",arr2)
"""

# indexing  : 
"""
a=np.array([10,20,30,40,50,60,70,80,90])
print(a)
print(a[2])  # index : start : 0 
print(a[2:5])
print(a[-1])
print(a[4 :-2])  # start 4 end -2 
print(a[4 :])  # start 4 
print(a[-2 :])  # start -2 
print(a[-2 : -5 :-1])  # start -2 
print(a[-5 : -2])  # start -2 
"""
# 2d array : 
"""
b= np.array([
    [1,2,3],   # 0 
    [4,5,6],   # 1
    [7,8,9]    # 2 
])
"""
# print(b)
# print(b[2])
# print(b[1:3])
# print(b[1:3,0:1])  # row  slice : 1:3 col slice 0:1 
# print(b[1:2,1:2])   # row 1:2 

# 3d array  : 

"""c=np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [11,12],
        [13,14]
    ]
])
print(c)
print(c[1,1,1])
"""

# extra : 

"""
a=np.arange(1,33).reshape(2,2,2,4)
print(a)
print(a[1,1,1,1])
"""

#boolean indexing : condition  apply  

"""a=np.array([1,-2,3,-4,5,6])
print(a)
print(a>0)
result =a[a<0]
print(result)
"""
# negative  value replace  with 10 : 
"""
a[a<0]=10
print(a)
"""

# 2d array :
"""
b= np.array([
    [1,-2,3],   # 0 
    [4,5,6],   # 1
    [7,8,-9]    # 2 
])

# print  only  negative value 
# print(b[b<0])
   
# b[b<0]=100
# print(b<0)
"""
# fancy  indexing  : 

"""a=np.array([10,20,30,40,50,60,70,80,90])
print(a[3])  # indexing  
print(a[2:5])  # slicing 
print(a[[2,5,6]])   # fancy indexing
"""

# 2d array : 
"""b= np.array([
    [1,-2,3],   # 0 
    [4,5,6],   # 1
    [7,8,-9]    # 2 
])
print(b)
print(b[[1,2],[0,2]])
"""
# broadcasting  : 

# case :1 
"""
a=np.array([1,2,3,4,5,6])
result = a*2
print(result)
"""
# case 2 : 
"""a=np.array([1,2,3,4,5,6])
b=np.array([
    [2],
    [4],
    [6]
])
print(a)
print(b)
print(a.shape)
print(b.shape)
print(b+a)
"""
# case 3 : 
a=np.array([
    [1,2,3],  
    [4,5,6],
    [7,8,9]
])
b= np.array([1,2,3,4,5,6,7,8,9])

print(a)
print(b)
print(a*b)

