#Sequence of number
import numpy as np
arr=np.arange(1,10,2)
print(arr)

#Creating Identity matrix
matrix=np.eye(4)
print(matrix)

#Some attributes
attr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(attr.shape)
print(attr.size)
print(attr.ndim)
print(attr.dtype)

#Converting datatype
a=np.array([1,2,3,4,5,6,7])
b=a.astype(float)
print(b)

#Mathematical operations
print(a+5)
print(a-5)
print(a*5)
print(a//5)
print(a%5)

#Aggregation funcction
c=np.sum(a)
print(c)
d=np.mean(a)
print(d)

#Slicing
a2=np.array([10,20,30,40,50,60,70,80,90,100])
print(a2[0:10:4])
print(a2[2:7:2])

#reshaping
print(attr.ravel())
print(attr.flatten())
new=np.insert(attr,2,[4,6,8])
print(new)

#splitting
print(np.split(new,3))

#Handling Missing values
missing=np.array([1,2,np.nan,4,5,np.nan,7,8,np.nan])
print(np.isnan(missing))
missing2=np.nan_to_num(missing,nan=200)
print(missing2)
