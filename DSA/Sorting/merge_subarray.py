def merge(arr, low, mid, high):
    left = arr[low: mid+1]
    right = arr[mid+1: high+1]
    i = 0
    j = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [3, 2, 1]
merge(arr, 0, len(arr)//2, len(arr))
print(arr)
