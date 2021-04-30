def selectionsort(l):
    n = len(l)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if l[j] < l[min_ind]:
                min_ind = j
        l[i], l[min_ind] = l[min_ind], l[i]


arr = [9, 4, 1, 7, 8, 3]
selectionsort(arr)
print(arr)
