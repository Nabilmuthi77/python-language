class mahasiswa_ubsi :
    def __init__(self,nama,jurusan,ipk):
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk
    def tampilkan_profil(self):
        print("Nama         : ", self.nama)
        print("Jurusan      : ", self.jurusan)
        print("IPK          : ", self.ipk)
        print()

#membuat object pertama dari kelas mahasiswaa
mahasiswa1 = mahasiswa_ubsi("Nabil", "Sistem Informasi", 3.50)
mahasiswa2 = mahasiswa_ubsi("Aditya", "Sistem Informasi", 3.40)
mahasiswa1.tampilkan_profil()
mahasiswa2.tampilkan_profil()