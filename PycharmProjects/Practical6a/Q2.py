answer_list = ["C", "D", "B", "A", "B"]

highest = 0

while True:
    student_list = []
    for n in range(5):
        option = input("MCQ " + str(n+1) + ": ")
        student_list.append(option)

    count = 0
    for i in range(5):
        if answer_list[i] == student_list[i]:
            count += 1
    print("Correct answers: ", count)
    if count > highest:
        highest = count
    option = input("Do you want to try again? (Y/N) ")
    if option.lower() == "n":
        print("")
        exit()
    elif option.lower() == "y":
        continue
    while option.lower() != "y" or "n":
        print("Invalid option.")
        exit()
    print("You have", highest, "correct answers.")
