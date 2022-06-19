def merge_sort(x):
    print("Bilangan diurutkkan ", x)
    if len(x)>1:
        mid = len(x)//2
        lefthalf = x[:mid]
        righthalf = x[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                x[k] = lefthalf[i]
                i = i+1
            else:
                x[k] = righthalf[j]
                j = j+1
            k = k+1
        while i < len(lefthalf):
            x[k] = lefthalf[i]
            i = i+1
            k = k+1
        while j< len(righthalf):
            x[k] = righthalf[j]
            j = j+1
            k = k+1
            print("Merging", x)
x = [22,10,15,3,8,2]
merge_sort(x)
print(x)