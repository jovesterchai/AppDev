sum = 0
num = int(input("Enter number: "))
if num<2:
    print("Number is less than two.")
    exit()
for i in range(num+1):
    if i%2==0:
        sum+=i
print(sum)
