jarak = int(input("Masukkan jarak: "))
karakter = input("Masukkan Karakter: ")
for i in range(int(jarak)):
    for o in range(0,10-i):
        print(" ", end=" ")
    for p in range(0, 2 * i + 1):
        print(karakter, end=" ")
    print()