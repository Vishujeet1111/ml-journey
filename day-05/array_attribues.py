import numpy as np 

arr_1d = np.array([[10,20,30]])

arr_3d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print(arr_1d.ndim)

print(arr_3d.ndim)

print(arr_1d.shape)
print(arr_1d.size)
print(arr_1d.itemsize)
print(arr_1d.dtype)