str1 = input("Enter a string: ")
print("Length of string:", len(str1))

if str1.isalnum():
    print("String contains alphanumeric.")
elif str1.isdigit():
    print("String contains only digits.")
elif str1.isalpha():
    print("String contains only alphabetic characters.")

if str1.islower():
    print("The letters in the string are all in lowercase.")
elif str1.isupper():
    print("The letters in the string are all in uppercase.")

if str1.isspace():
    print("String only contains whitespace characters.")
