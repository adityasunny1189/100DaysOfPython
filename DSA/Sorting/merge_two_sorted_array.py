def merge(l1, l2):
    i = 0
    j = 0
    arr = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            arr.append(l1[i])
            i += 1
        else:
            arr.append(l2[j])
            j += 1

    while i < len(l1):
        arr.append(l1[i])
        i += 1
    while j < len(l2):
        arr.append(l2[j])
        j += 1
    return arr


l1 = [2, 4, 7, 9, 14]
l2 = [3, 5, 9, 15, 18, 66, 89]
ans = merge(l1, l2)
print(ans)
