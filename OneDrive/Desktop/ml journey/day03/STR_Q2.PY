S = "VISHUJEET SHARMA "
print(S[: : -1])


# palindrome 
a = (input("enter a word "))
reverse_string = a[::-1]

if a == reverse_string :
    print(f"word is a palindrome {a}")
else:
    print("Word is not a palindrome")