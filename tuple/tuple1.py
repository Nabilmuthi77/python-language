# membuat tuple kosong
my_tuple = ()
print(my_tuple)

# tuple dengan 1 elemen
# output : (1,)
my_tuple = (1,)
print (my_tuple)

# tuple berisi integer
# output : (1, 2, 3)
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple bersarang
# output : ("hello", [1,2,3], (4,5,6))
my_tuple = ("hello", [1,2,3], (4,5,6))
print(my_tuple)

# tuple bisa juga tidak menggunakan  tanda ()
# output : (1,2,3)
my_tuple = 1,2,3

# memasukkan anggota tuple ke variabel yg bersesuaian
# a akan berisi 1, b akan berisi 2, c akan berisi 3
# output : 1 2 3
a, b, c = my_tuple
print (a, b, c)