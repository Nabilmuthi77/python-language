def faktorial (n):
	if n <= 1:
		return 1
	else:
		return n*faktorial (n-1)
i = 0
x = int(input("Masukkan Bilangan: "))
while i<=x:
	print(i,'! = ', faktorial (i))
	i+=1