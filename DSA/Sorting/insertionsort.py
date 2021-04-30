def insertionsort(arr):
    n = len(arr)
    for i in range(1, n):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x


arr = [9, 6, 8, 3, 2, 5, 1]
insertionsort(arr)
print(arr)
