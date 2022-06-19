N = int(input("Masukan jumlah simbol: "))
simbol = input("Masukkan simbol: ")
for A in range(int(N)):
    for L in range(0, 10-A):
        print("", end=" ")
    for Y in range(0, 1 * A + 1):
        print(simbol, end=" ")
    print()