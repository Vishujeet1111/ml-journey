# skip the 5 iteration 

n = int(input("enter a no : "))

for i in range(1,11):
    if i == 5:
        continue
    print(n, 'x' ,i, '=',n*i)
