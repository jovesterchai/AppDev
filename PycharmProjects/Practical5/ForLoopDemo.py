sum = 0
num = int(input("Enter number: "))
if num < 2:
    print("Number is less than 2.")
    exit()
for i in range(1, num+1):
    sum = sum + i
print(sum)

#################################################################

sum = 0
i = 1
num = int(input("Enter number: "))
if num < 2:
    print("Number is less than 2.")
    exit()
while i <= num:
    if i % 2 == 0:
        sum = sum + 1
    i += 1
print(sum)
