for i in range(6):
    for j in range(i+1):
        if i == j or j == 0:
            print("#", end="")
        else:
            print(" ", end="")
    print()
