print(" ")
print("--------------------------------------")
print("PROGRAM HITUNG GAJI KARYAWAN")
print("--------------------------------------")
print("              ")
gaji_pokok = 300000
nam_kar = input("Nama Karyawan    : ")
#-----------------------------------
gol_jab = input("Golongan Jabatan : ")
if gol_jab == "1":
    tun_jab = 0.05 * gaji_pokok
elif gol_jab == "2":
    tun_jab = 0.10 * gaji_pokok
else :
    tun_jab = 0.15 * gaji_pokok
#-----------------------------------
pdk = input("Pendidikan       : ")
if pdk == "SMA" or pdk == "sma":
    tun_pdk = 0.025 * gaji_pokok
elif pdk == "D1" or pdk == "d1":
    tun_pdk = 0.05 * gaji_pokok
elif pdk == "D3" or pdk == "d3":
    tun_pdk = 0.2 * gaji_pokok
else :
    tun_pdk = 0.3 * gaji_pokok
#----------------------------------
jum_ker = int(input("Jumlah Jam Kerja : "))
if jum_ker > 8:
    honor = ((jum_ker) - 8) * 3500
else :
    honor = 0
#-----------------------------------
print("--------------------------------------")
print("Karyawan yang bernama : ", (nam_kar))
print("\nHonor yang diterima")
print("Tunjangan jabatan     : Rp ", float (tun_jab))
print("Tunjangan Pendidikan  : Rp ", float (tun_pdk))
print("Honor Lembur          : Rp ", int (honor))
tunjangan = tun_jab + tun_pdk
total_gaji = gaji_pokok + tunjangan + honor
print("--------------------------------------")
print("Total Gaji            : Rp ", str (total_gaji))
print("(Gaji Pokok + Tunjangan + Lembur)")
print("         ")