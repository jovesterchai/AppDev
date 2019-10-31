str1 = input("Enter a string: ")

index = 0
for letter in str1:
    if index % 2 == 0:
        print(letter.upper(), end="")
    else:
        print(letter, end="")
    index += 1
