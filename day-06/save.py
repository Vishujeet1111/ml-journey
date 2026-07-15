import pandas as pd 

data = {"Name" : ["Vishujeet Sharma"],
        "Age" : [17],
        "City": ["Delhi"] 
        }

df = pd.DataFrame(data)
# print(df)

# df.to_csv("output.csv")
# df.to_excel("output.xlsx")
# df.to_json("output.json")

print(df.info())
