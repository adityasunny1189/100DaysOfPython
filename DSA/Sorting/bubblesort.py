def bubblesort(l):
    n = len(l)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


arr = [9, 2, 5, 1, 7]
print(arr)
bubblesort(arr)
print(arr)
