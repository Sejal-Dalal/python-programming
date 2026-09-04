while True:
    name=input("Enter the name of customer:")
    total=0
    while True:
        print("enter the amount and quantity")
        amount=float(input("enter the amount:"))
        quantity=int(input("enter the quantity:"))
        total+=amount*quantity
        repeat = input("do you want to add more item?(yes/no)")
        if repeat=="no" or repeat=="No":
            break
    print("*"*40)
    print("Name:",name)
    print("Total:",total)
    print("*"*40)
    print("******HAPPY SHOPPING*****")
    repeat1 = input("do you want to switch to next customer?(yes/no)")
    if repeat1=="no" or repeat1=="No":
        break