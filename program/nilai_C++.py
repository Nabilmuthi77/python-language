import pandas as pd

nim = []
nama = []
uts = []
uas = []
hasil =[]
huruf =[]

tahu_aci = 2

for i in range (tahu_aci) :
	print ("Data Ke- "+ str (i+1))
	nim.append(input("NIM : "))
	nama.append(input("Nama : "))
	uts.append(int(input("Nilai UTS : ")))
	uas.append(int(input("Nilai UAS : ")))

for i in range (tahu_aci) :
	hasil.append((uas[i]*0.4 + uts[i]*0.6))

for i in range (tahu_aci) :
	if hasil [i] >= 80 :
		huruf.append("A")
	elif hasil [i] >= 70 :
		huruf.append("B")
	elif hasil [i] >= 56 :
		huruf.append("C")
	elif hasil [i] >= 47 :
		huruf.append("D")
	else :
		huruf.append("E")

dt = {
	"NIM" : nim,
	"Nama Lengkap" : nama,
	"Nilai UTS" : uts,
	"Nilai UAS" : uas,
	"Nilai Hasil" : hasil,
	"Nilai Huruf" : huruf
}

data = pd.DataFrame(dt)

print ("\t\t Daftar Nilai Kuliah C++ ")
print ("*****************************************************")
print (data)
print ("*****************************************************")