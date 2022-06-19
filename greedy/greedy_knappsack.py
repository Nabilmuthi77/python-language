def fractional_knapsack (value, weight, capacity) :
    index = list(range(len(value)))
    ratio = [v/w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0]*len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_value += value[i]*capacity/weight[i]
            break

    return max_value, fractions

n = int(input("Berapa banyak angka nya (n) = "))
value = input("Masukkin nilai Pi dari {} banyaknya angka tadi = ".format(n)).split()
value = [int(v) for v in value]
weight = input("Masukkin nilai Wi dari {} banyaknya angka tadi = ".format(n)).split()
weight = [int(w) for w in weight]
capacity = int(input("Masukkan kapasitas maksimal (M) = "))
max_value, fractions = fractional_knapsack(value, weight, capacity)
print("Nilai profit maksimal = ", max_value)
print("yang nilai nya diambil dari : ", fractions)