import pandas as pd

data = { 
    "Name" : [ "Ram","Vishujeet","Shyam","radha","krishna","sita","hanuman","angad","parladh ji "],
    "Age" : [111,17,50,45,80,74,75,42,52],
    "Salary" : [ 4000,500,71,70,82,100,480,900,850],
    "Performance Score" : [100,15,100,100,14,152,100,48,50]

}

df = pd.DataFrame(data)
# high_salary = df[df["Salary"] > 5]
# print(high_salary)

filter = df[(df['Age'] > 30)  & (df [ 'Salary'] > 100)]
print(filter)