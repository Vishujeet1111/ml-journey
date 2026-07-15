sentence = input("enter the senetence :  ")

vowel = ["A","a","E","e","i","I","o","O","U","u"]
count = 0
for i in sentence:
    if i in vowel:
      count += 1
print(count) 
