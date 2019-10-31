num = int(input("Enter number: "))
i = 0
while num > 0:
    i += num
    num = int(input("Enter number: "))
else:
    print("The sum of your numbers is", i)

