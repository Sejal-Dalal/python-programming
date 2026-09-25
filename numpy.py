#IMPORTING NUMPY
python_list=[1,2,3,4,5,6,7,8,9,10]
print(python_list)
import numpy as np
numpy_list=np.array([1,2,3,4,5,6,7,8,9,10])
print(numpy_list)

#CREATING ARRAY
import numpy as np
list1=[1,2,3,4,5,6]
print(list1)
arr_list1=np.array(list1)
print(arr_list1)
print(type(arr_list1))

#1 DIMENSIONAL ARRAY
array_1d=np.array([1,2,3,4,5,6,7,8,9,10])
print(array_1d)
#2 DIMENSIONAL ARRAY
array_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array_2d)

#FUNCTION -ZEROS
array=np.zeros((3,4))
print(array)

#FUNCTION- ONEA
a=np.ones((3,4))
print(a)

#FUNCTION-FULL
b=np.full((3,4),7)
print(b)
