n = int(input("Masukkan Jumlah Piringan : "))
def hanoi (x, A, B, C) :
    if x == 1 :
        print("Pindahkan dari", A, "ke", C)
    elif x<= 0 :
        print("Jumlah Piringan Tidak Sesuai")
    else :
        hanoi (x-1, A, C, B)
        print("Pindahkan dari", A, "ke", C)
        hanoi (x-1, B, A, C)
hanoi (n, "A", "B", "C")