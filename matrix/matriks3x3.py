import numpy as np
a = np.zeros((3,3))
a[0][0] = 1
a[0][1] = 2
a[0][2] = 3
a[1][0] = 4
a[1][1] = 5
a[1][2] = 6
a[2][0] = 7
a[2][1] = 8
a[2][2] = 2
print("a = ")
print(a)
print("")

b = np.ones((3,3))
b[0][0] = 1
b[0][1] = 2
b[0][2] = 3
b[1][0] = 4

print("b = ")
print(b)
print("")

print("c = ")
print(a+b)