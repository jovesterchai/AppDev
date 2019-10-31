for i in range(6):
    for j in range(i+1):
        if i == j:
            print("#", end="")
        else:
            print(" ", end="")
    print()
