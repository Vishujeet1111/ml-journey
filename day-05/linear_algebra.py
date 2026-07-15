import numpy as np 

a = np.array([[1,2,3], [4,5,6],[5,4,6]])
b = np.array([[7,8,9],[1,5,9],[1,4,7]])

result = np.dot(a,b)
print(result)

transpose = a.T
det = np.linalg.det(a)
inverse = np.linalg.inv(a)
print(transpose)
print(det)
print(inverse)