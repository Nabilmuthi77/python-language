#Bagian inputan
nis = input("Input NIS: ")
nama = input("Input Nama Siswa: ")
jurusan = input("Input Jurusan [SI/SIA]: ")

#proses
if jurusan == "si" or jurusan == "SI":
    nm_prodi = "Sistem Informasi"
    harga = 2400000
else:
    nm_prodi = "Sistem Informasi Akuntansi"
    harga = 2000000

#Bagian Output
print ("---------------------------")
print ("FORM PENDADTARAN")
print ("---------------------------")
print ("NIS  : ", str (nis))
print ("Nama : ", str (nama))
print ("Nama Prodi : ", str (nm_prodi))
print ("Harga : ", str (harga))
print ("---------------------------")