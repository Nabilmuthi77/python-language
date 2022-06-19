import ryuuchi as jas
class login :
    def karyawan (self):
        pass
    def __init__(self,nip,nama):
        self.nip = nip
        self.nama = nama
    def profil(self):
        print('+'*37)
        print("Kasir Kedai Coffee JAS")
        print('+'*37)
        print("NIP           :",self.nip)
        print("Nama Kasir    :",self.nama)
        print('+'*37)

nama_karyawan = login(input("Masukkan NIP : "), input("Nama Lengkap : "))
nama_karyawan.profil()

pilihan = 'y'
while pilihan != 'n' :
    print('_'*37)
    print(jas.df.rename(columns = {'abc': "Menu coffee"}, index = {0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10}))
    print('_'*37)
    print('_'*37)
    nama_pembeli = input("Nama Pembeli : ")
    pesan = (int(input("Pilih Menu Coffee = ")))
    jumlahpesan = (int(input("Masukkan Jumlah Order = ")))
    if pesan == 1 :
        listnama = "Black Coffee Original"
        harga = (25000 * jumlahpesan)
        ppn= int(harga * 0.05)
        if jumlahpesan >= 3 :
            diskon = int(harga * 0.1)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = 0
            totalharga = int(harga + ppn)
    elif pesan == 2 :
        listnama = "Vietnam Drip"
        harga = (27000 * jumlahpesan)
        ppn = int(harga * 0.05)
        if jumlahpesan >= 3:
            diskon = int(harga * 0.1)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = 0
            totalharga =int(harga + ppn)
    elif pesan == 3 :
        listnama = 'Espresso'
        harga = int(28000 * jumlahpesan)
        ppn = int(harga * 0.05)
        if jumlahpesan >= 3:
            diskon = int(harga * 0.1)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = 0
            totalharga = int(harga + ppn)
    elif pesan == 4 :
        listnama = "Caffe Latte"
        harga = int(30000 * jumlahpesan)
        ppn = int(harga * 0.05)
        if jumlahpesan >= 3 :
            diskon = int(harga * 0.1)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = 0
            totalharga = int(harga + ppn)
    elif pesan == 5 :
        listnama = "Hazelnut Latte"
        harga = int(35000 * jumlahpesan)
        ppn = int(harga * 0.05)
        if jumlahpesan >= 3 :
            diskon = int(harga * 0.1)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = 0
            totalharga = int(harga + ppn)
    elif pesan == 6 :
        listnama = "Mocha Latte"
        harga = int(37000 * jumlahpesan)
        ppn = int(harga * 0.05)
        if jumlahpesan >= 3 :
            diskon = int(harga * 0.1)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = 0
            totalharga = int(harga + ppn)
    elif pesan == 7 :
        listnama = "White Choco Mocha"
        harga = int(40000 * jumlahpesan)
        ppn = int(harga * 0.05)
        if jumlahpesan >= 3 :
            diskon = int(harga * 0.1)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = 0
            totalharga = int(harga + ppn)
    elif pesan == 8 :
        listnama = 'Affogato'
        harga = int(40000 * jumlahpesan)
        ppn = int(harga * 0.05)
        if jumlahpesan >= 3 :
            diskon = int(harga * 0.1)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = 0
            totalharga = int(harga + ppn)
    elif pesan == 9 :
        listnama = "Choco Mint"
        harga = int(42000 * jumlahpesan)
        ppn = int(harga * 0.05)
        if jumlahpesan >= 3 :
            diskon = int(harga * 0.1)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = 0
            totalharga = int(harga + ppn)
    elif pesan == 10 :
        listnama = 'Delnaco'
        harga = int(43000 * jumlahpesan)
        ppn = int(harga * 0.05)
        if jumlahpesan >= 3 :
            diskon = int(harga * 0.1)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = 0
            totalharga = int(harga + ppn)
    else:
        listnama = '-'
        harga = '-'
        ppn = '-'
        diskon = '-'
        totalharga = '-'
        pilihan=input("Menu tidak tersedia, Apakah anda ingin order lagi? [Y/N] : ")
        continue
    print('-'*37)
    print("Kedai Coffe JAS")
    print('-'*37)
    print("Nama Pembeli  :", nama_pembeli)
    print("Menu Coffee   :", listnama)
    print("Jumlah Order  :", jumlahpesan)
    print("Cost          :", harga)
    print("Discount      :", diskon)
    print("PPN           :", ppn)
    print('-'*37)
    print("Jumlah Bayar    : %i" % (totalharga))
    paid = (int(input("Uang Bayar      : ")))
    back = paid - totalharga
    print("Uang Kembalian  : %i" % (back))
    print('-'*37)
    pilihan=input("Apakah anda ingin order lagi? [Y/N] : ")