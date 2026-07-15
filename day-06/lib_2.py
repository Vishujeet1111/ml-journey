import pandas as pd

s = pd.Series([10,20,40])
# print(s.dtype)
s.name = "number"
print(s)