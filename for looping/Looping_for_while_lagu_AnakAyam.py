a = int(input("Masukkan jumlah anak ayam: "))
kelompok2 = ["Kelompok 2: Sesilia | Nabil | Mayori | Ilham | rahma "]
print("")
print ("tek kotek kotek kotek")
if a >= 2:
    while a > 1:
        print("anak ayam turun %d mati 1 tinggal %d"%(a,a-1))
        a = a-1
    print ("__________________________________________________________")
    print (kelompok2)
else:
    print ("anak ayam turun %d mati 1 tinggal induknya"%(a))
    print ("__________________________________________________________")
    print(kelompok2)