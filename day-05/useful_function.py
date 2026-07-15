import numpy as np 

a = np.array([1,2,3,4])
b = np.array([2,4,6,8])
c = np.concatenate([a,b])
# print(c)

# stack 
stacked = np.stack([a,b])
# print(stacked)

# sort
arr_1 = np.array([9,8,74,5,41,4,4])
sort_ = np.sort(arr_1)
# print(sort_)

# unique
u = np.unique(arr_1)
print(u)

# where condition
arr = np.array([1,2,3,4,5])
result = np.where(arr>3,arr,0)
print(result)