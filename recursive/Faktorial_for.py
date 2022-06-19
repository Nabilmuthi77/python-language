def faktorial(bil):
  hasil = 1
  for x in range(2,bil+1):
    hasil = hasil * x
  return hasil
print("------------------------------------------------")
print('Menghitung bilangan faktorial mengguna for loop')
print("------------------------------------------------")
angka = int(input('Masukkan nilai faktorial : '))
faktorial_bil = faktorial(angka)
print('Bilangan faktorial dari {} adalah {}'.format(angka,faktorial_bil))
print("------------------------------------------------")