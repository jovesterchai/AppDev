firstStr = input("Enter first string: ")
secStr = input("Enter second string: ")

newFirstStr = firstStr[0:-1] + secStr[-1]
newSecStr = secStr[0:-1] + firstStr[-1]
print(newFirstStr)
print(newSecStr)
