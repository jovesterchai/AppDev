num_list = []
count = 1

while count <= 10:
    msg = "Enter number #" + str(count) + ": "
    try:
        num = int(input(msg))
        num_list.append(num)
        count += 1
    except ValueError:
        print("You have enter an invalid number, please try again.")


print("The lowest number is :", min(num_list))
print("The highest number is :", max(num_list))
print("The total is :", sum(num_list))
average = sum(num_list)/len(num_list)
print("The average is ", average)
