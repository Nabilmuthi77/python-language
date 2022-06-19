ulang = 2
for i in range(ulang):
    print("data ke - "+ str (i+1))
    nama = input("Masukkan NIM Anda: ")
    uts = int(input("Masukkan nilai UTS anda : "))
    uas = int(input("Masukkan nilai UAS anda : "))
    print ("Nim Anda adalah %s Nilai UTS anda %i Nilai UAS anda %i" % (nama, uts, uas))
    print("--------------------------------------\n")