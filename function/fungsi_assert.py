# untuk mengoreksi kesalahan dalam coding
# rumus nya: assert <condition>, 'statement'
#(contoh 1)
def umur (age):
    assert age > 0, "Bukan Negative"
    print ("Oke Your Age is :", age)

umur(20)
#coba umur(-1)

#(contoh 2)
assert 'selenium' in "selenium is web for automation", "Validation failed"
print("Validation passed")
#coba 'Zelenium'

#(contoh 3)
str1 = 'python'
str2 = 'python'
assert str1 == str2, "string matching failed"
print("Validation 2 passed")
#coba str2 = 'java'

#(contoh 4)
import kosong5

assert kosong5.a, "Salah woii"
print("Validation passed")
#coba ganti di folder kosong5.py 3*3a