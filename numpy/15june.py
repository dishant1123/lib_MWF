import  numpy as np
"""
1. maths : + - * / 
2. stats function  : mean , std , var , sum , max , min , argmax , argmin ,
3. linear algebra  : inv , det ,T 
4. loadtxt , genfromtxt 
5.random  module  
6.matrix multiplication
7. flattern ,ravel 
"""

# maths  : 

"""
a=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
b=np.array([
    [11,12,13],
    [14,15,16],
    [17,18,19]
])

print(a+b)   # element  wise  :  1+11  , 2+12 ,3+13 
print(a-b)
print(a*b)  # element  wise  :  1*11  , 2*12 ,3*13   it is  not  matrix  multiplication
print(a/b)
print(a%b)
print(a//b)  # floor divi  :  int  
"""
# matrix  multiplication  :dot () , a@b , matmul()

"""
a=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
b=np.array([
    [11,12,13],
    [14,15,16],
    [17,18,19]
])
print(a.dot(b))
print(a@b)
result =np.matmul(a,b)
print(result)
"""

# stats function  : mean , std , var , sum , max , min , argmax , argmin ,argsort 
"""a=np.array([1,2,3,4,5,6,7,8,9])

print(a.mean())
print(np.median(a))
print(np.std(a))
print(np.var(a))
print(np.sum(a))
"""
"""
a=np.array([
    [11,22,3],
    [4,55,6],
    [7,8,79]
])
"""
# print(a.sum())
# print(a.sum(axis=0))  # col wise sum  
# print(a.sum(axis=1))  # row wise sum  

# print(a.max())
# print(a.max(axis=0))
# print(a.max(axis=1))
# print(a.argmax())
# print(a.argmax(axis=0))  # index number of  max value  ===> col  
# print(a.argmax(axis=1))  # index number of  max value  ===> row 

# print(a.min())
# print(a.min(axis=0))
# print(a.min(axis=1))
# print(a.argmin())
# print(a.argmin(axis=0))  # index number of  min value  ===> col
# print(a.argmin(axis=1))  # index number of  min value  ===> row

# result =np.sort(a)
# print(result)

# linear algebra  : inv , det ,T
"""
a=np.array([
    [11,22,3],
    [4,55,6],
    [7,8,79]
])
print(a.T)  # transpose
print(np.linalg.inv(a))
print(np.linalg.det(a))
"""

# flatten   and ravel : convert in to  1d array  

# flatten : it is  similar as .copy()

"""a=np.array([
    [11,22,3],
    [4,55,6],
    [7,8,79]
])

print("original array : \n",a)

x= a.flatten()
x[2] =900

print("original array : \n",a)
print("flatten array : \n",x)
"""
# ravel  :  it is  similar  as slicing  and shallow  copy  create  new  object  memory shared .
"""a=np.array([
    [11,22,3],
    [4,55,6],
    [7,8,79]
])

print("original array : \n",a)

x= a.ravel()
x[2] =900

print("original array : \n",a)
print("flatten array : \n",x)
"""

# vstack  : vertical stacking

"""a=np.array([1,2,3,4,5])
b=np.array([
    [11,12,13],
    [14,15,16],
    [17,18,19]
])

print(np.vstack(a))
print(np.hstack(a))
print(np.hstack(b))
"""
# concatenate  :

"""a=np.array([1,2,3,4,5,6])
b=np.array([6,7,8,9,10])

result= np.concatenate((a,b))
print(result)

result1 =np.split(a,3)
print(result1)
"""

# loadtxt : only number , data  clean

"""
a=np.loadtxt("numpy\sample.txt",dtype=int,usecols=(0),skiprows=1,encoding="utf-8")
print(a)
"""
# genfromtxt : missing value 

"""
b=np.genfromtxt("numpy\sample2.txt",dtype=None,delimiter=",",filling_values=10000,skip_header=0,names=True)
print(b)
"""

# dstack :
a=np.array([1,2,3,3,4,5])
b=np.array([[
    [11,12,13],
    [14,15,16],
    [17,18,19]
]])

# print(np.dstack(a))
print(np.dstack(b))