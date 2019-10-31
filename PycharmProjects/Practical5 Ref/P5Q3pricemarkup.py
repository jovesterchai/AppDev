price=float(input("Enter the price of the item:$"))
while price>0:
    sellprice=price*1.25
    print("The markup price is $%.2f"%sellprice)
    price=float(input("Enter the price of the item:$"))
print("Now exiting...")
