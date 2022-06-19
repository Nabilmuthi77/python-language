#contoh 1
def fungsiHello1():
    print("Hello world")

fungsiHello1()

def fungsiHello2():
    return "Hello world"

x = fungsiHello2()
print(x)

#contoh 2
def luas_persegi_panjang1(panjang, lebar):
    luas = panjang*lebar
    print ("Luas persegi panjang :", luas)

luas_persegi_panjang1(8,4)

def luas_persegi_panjang2(panjang, lebar):
    luas = panjang*lebar
    return luas

print("Luas persegi panjang : %d" % luas_persegi_panjang2(8,4))

#contoh 3 yg sering salah
def ucapan():
    print("Nama saya wilson")
print(ucapan())

def ucapan ():
    return print("Nama Saya Wilson")
blueprint = ucapan()
print(blueprint)

#contoh 4
def kali_print(a,b):
    print(a*b)

kali_print(5,4)
print(kali_print)

def kali_return(a,b):
    return a*b

x = kali_return(5,5)
print(x)

