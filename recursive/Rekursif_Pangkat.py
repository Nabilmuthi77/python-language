def pangkat (x,y):
    if y == 0:
        return 1
    else :
        return x * pangkat (x,y-1)

x = int(input("Masukkan Nilai X : "))
y = int(input("Masukkan Nilai y : "))

print ("%d dipangkatkan %d = %d" % (x,y,pangkat(x,y)))