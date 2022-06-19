makanan = [ ] #variabel untuk menampung wadah array
stop = False #untuk eksekusi while looping
i = 1 #memulai penomoran

while(not stop): #alt stop != False
    makanan_favorite = input("Silakan inputkan Makanan favoritmu yang ke- {}: ".format(i))
    makanan.append(makanan_favorite) #menambah jumlah elemen + bisa menghitung semua yg kita inputkan
    i += 1 # Increment i
    pilihan = input("Ada lagi? (y/t): ")
    if(pilihan == "t"):
        stop = True #back stop = False

# Cetak Semua Makanan
print ('=' * 10)
print ("Kamu punya {} makanan favorit :".format(len(makanan)))
for x in makanan:
    print ("- {}".format(x))


#UBSI