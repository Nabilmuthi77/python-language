mat1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
mat2 = [
    [1,2,3],
    [4,1,1],
    [1,1,2]
]

for x in range (0, len(mat1)):
    for y in range (0, len(mat1[0])):
        print(mat1[x][y] + mat2[x][y], end=' '),
        print
        