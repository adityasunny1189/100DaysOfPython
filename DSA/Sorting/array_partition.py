def partition(arr, ind):
    helper = [arr[ind]]
    for i in range(len(arr)):
        if i == ind:
            continue
        elif arr[i] > arr[ind]:
            helper.append(arr[i])
        else:
            helper.insert(0, arr[i])
    for i in range(len(helper)):
        arr[i] = helper[i]


def lomuto_partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i + 1


def hoares_partition(arr, start, end):
    pivot = arr[start]
    i = start - 1
    j = end + 1
    while True:
        i = i + 1
        while arr[i] < pivot:
            i += 1
        j = j - 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, start, end):
    if start < end:
        p = lomuto_partition(arr, start, end)  # or p = hoares_partition(arr, start, end)
        quick_sort(arr, start, p - 1)
        quick_sort(arr, p + 1, end)


a = [9, 10, 13, 6, 8, 7]
print(f"Before Partition: {a}")
quick_sort(a, 0, len(a) - 1)
print(f"After Partition: {a}")
