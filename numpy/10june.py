# numpy  :  pip install numpy  
"""
1 string  2. list  3 tuple  4 set  5 dict 

numpy  : 
why  is important in DS / DA ? 

1. num operation 
2. faster 
3. statistics 
4. time  
5. matrix 

"""
# create array  : 
import  numpy as np 

"""a= np.array([1,2,3,4,5,6])
print(a)
print(a.ndim)  # number dimenstional 
a[2] =90
print(a)

b= np.array([
    [1,2,3], 
    [4,5,6]
])
# print(b)
print(b.ndim)
# b[1] =90 
# print(b)
# b[1,2] =900  # row  1, col 2
b[0,0] =400  # row  0, col 0
print(b)
"""

# array  attributes  : ndim shape itemsize dtype 

"""arr =np.array([1,2,3,90,901])

b= np.array([
    [1,2,3], 
    [4,5,6]
])
print(arr)
print(arr.dtype)  # int 
print(arr.ndim)  # 1 
print(arr.shape)  # 
print(b.shape)
print(arr.itemsize)
"""

# method  : np.one , np.zero ,np.full , np.arange , np.linspace

"""a=np.arange(10)  # start , stop  ,step  :1,11 ,2 
print(a) 

b= np.arange(1,10,3)  # start  :1  end :10  step :3 
print(b)

# c= np.ones(10,dtype=int)  # 10
c= np.ones((3,2),dtype=int)  # 10   3 row  2  col 
print(c)

# d =np.zeros(10,dtype=int)  # 10
d =np.zeros((2,3),dtype=int)  # 10
print(d)

e= np.full((2,3),100,dtype=int)  # 100
print(e)

f= np.linspace(1,10,3)
print(f)
"""
# formula  : 
"""
stop -start /step -1    #10 -1 / 3-1 ===>4.5 
"""

# reshape : 

"""a=np.arange(10)
print(a)
print(a.reshape(2,5))

b= np.ones(10).reshape(5,2)
print(b)
"""

# identity  matrix : 
"""
1 0 0   (0,0)1  (0,1)0  (0,2)0  
0 1 0 
0 0 1

"""
"""a=np.eye(3)
print(a)
"""
# transpose  :

"""b= np.arange(9).reshape(3,3)
print(b)
transpose = b.T
print(transpose)
"""

# list  : 
l1= [1,2,3,4,5] 
# l2 =l1
l2 =l1.copy()
l2[2] =900 
print("l1 is  : ",l1)
print("l2 is  : ",l2)
# y,j ,s,m: l2 change  l1 not 
# v,p,d,s ,k,s     both changes

"""
task  :1 reshape 1d   ===> convert  2d 
task  :2  list  : one letter and  last letter same  then append in another  list. and len must  be  more than 3  

input  :l1 = ["aba" ,"1221" ,"php","python","xyz"]
output  : l1=["aba" ,"1221" ,"php"]

"""
