# kode ini bisa digunakan untuk selection sort
# dan buble sort
def selection_sort(val):
    for i in range(len(val)-1,0,-1):
        max = 0
        for j in range (1, i+1):
            if val[j]>val[max]:
                max = j
        temp = val[i]
        val[i] = val[max]
        val[max] = temp
angka = [22,10,15,3,8,2]
selection_sort(angka)
print(angka)