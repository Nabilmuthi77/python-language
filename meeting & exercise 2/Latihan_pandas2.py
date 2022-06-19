import pandas as pd
list_nama = []
list_uts = []
list_uas = []
nilai_hasil = []
nilai_huruf = []

repeat = 2
for i in range (repeat):
    print ("data ke - "+ str (i+1))
    list_nama.append(input("Nama : "))
    list_uts.append(int(input("Nilai UTS : ")))
    list_uas.append(int(input("Nilai UAS : ")))

for i in range (repeat):
    nilai_hasil.append((list_uas[i]*0.4 + list_uts[i]*0.6))

for i in range (repeat):
    if nilai_hasil [i] >= 80 :
        nilai_huruf.append("A")
    elif nilai_hasil [i] >= 70 :
        nilai_huruf.append("B")
    elif nilai_hasil [i] >= 56 :
        nilai_huruf.append("C")
    elif nilai_hasil [i] >= 47 :
        nilai_huruf.append("D")
    else :
        nilai_huruf.append("E")

mahasiswa = {
    " Nama Mahasiswa" : list_nama,
    "Nilai UTS" : list_uts,
    "Nilai UAS" : list_uas,
    "Nilai Hasil" : nilai_hasil,
    "Nilai Huruf" : nilai_huruf
}
data_mhs = pd.DataFrame(mahasiswa)
print("\t\tDaftar Nilai Mata Kuliah C++")
print("===============================================================")
print(data_mhs)
print("===============================================================")