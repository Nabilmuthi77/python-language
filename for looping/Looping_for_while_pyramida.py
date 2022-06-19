for i in range(0,5):
    for o in range(0,20-i):
        print(" ", end=" ")
    for p in range(0, 2 * i + 1):
        print("*", end=" ")
    print()