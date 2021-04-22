def first_occurrence(arr, ele):
    ans = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > ele:
            high = mid - 1
        elif arr[mid] < ele:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1
    return ans


def last_occurrence(arr, ele):
    ans = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > ele:
            high = mid - 1
        elif arr[mid] < ele:
            low = mid + 1
        else:
            ans = mid
            low = mid + 1
    return ans


print(first_occurrence([8, 10, 10, 10, 10, 20], 10))
print(last_occurrence([8, 10, 10, 10, 10, 20], 10))



