while True:
    cost = float(input("Enter cost price: "))
    if cost <= 0:
        break
    print("The retail price is %.2f" % (cost*1.25))
