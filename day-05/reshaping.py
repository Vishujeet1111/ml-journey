import numpy as np 

arr_1d = np.arange(12)
reshaped = arr_1d.reshape(3,4)

# print(reshaped)

flattened = reshaped.flatten()
print(flattened)