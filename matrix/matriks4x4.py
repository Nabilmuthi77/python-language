matriks = ([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])
for i in range(4):
    for j in range(4):
        if i == j:
            matriks[i][j]=1 #diagonal atas kiri ke kanan
        if i < j:
            matriks[i][j]=1 #segitiga atas kanan
        if i > j:
            matriks[i][j]=0 #segitiga bawah kiri
for i in range(4):
    print(matriks[i])