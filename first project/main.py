expense = []
print("Welcome to Hisab kitab 📝 ")
while True:
    print("===MENU===")
    print("1. Add all expense")
    print("2. View all expense")
    print("3. View total spending")
    print("4. Exit")

    choice = int(input("print you  choice : "))
    if(choice == 1):
        date = (input("enter you date  in DD/MM/YYYY : "))
        category = input("enter the category of purchase  ex food ,travel etc : " )
        description = input("enter the specific object u purchase form were  : ")
        amount = float(input("enter the amount : "))

        expenses = {
            "date": date,
            "category": category, 
            "description": description,
            "amount": amount,
        }

        expense.append(expenses)
        print("Expense added sucessfully ☺️")
    elif(choice == 2):
        if(len(expense) == 0):
            print("NO expense added : 😅")
        else:
            print("====YOUR EXPENSE=====")
            count = 1
            for spent in expense:
                print(f"kharcha no {count} ~> ,{spent ['date']} , {spent ['category']}  ,{spent ['description']} , {spent['amount']}")
                count = count + 1


    elif(choice == 3):
        total = 0
        for spent in expense:
            total = total + spent["amount"]

        print("Total expense : ",total)


    elif(choice == 4 ):
        print("thanks for using our system : ")
        break
    else:
        print("You are choose invalid no : ")

