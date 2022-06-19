def insertion_sort(val):
    for index in range(1,len(val)):
        a = val[index]
        b = index
        while b>0 and val[b-1]>a:
            val[b]=val[b-1]
            b = b-1
            val[b] = a
angka = [22,10,15,3,8,2]
insertion_sort(angka)
print(angka) 