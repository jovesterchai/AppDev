num_list = []

number = int(input("How many numbers to capture: "))

for i in range(number):
    msg = "Enter number #" + str(i+1)
    num = int(input(msg))
    num_list.append(num)

print("The lowest number is :", min(num_list))
print("The highest number is :", max(num_list))
print("The total is :", sum(num_list))
average = sum(num_list)/len(num_list)
print("The average is ", average)
