# Even no list
even_list = [i for i in range(100) if i % 2 == 0]
# print(even_list)


def get_max(arr):
    max_ele = 0
    for i in arr:
        if i > max_ele:
            max_ele = i
    return max_ele


def sec_max(arr):
    max_ele = 0
    sec_max_ele = 0
    for i in arr:
        if i > max_ele:
            sec_max_ele = max_ele
            max_ele = i
        elif i == max_ele:
            continue
        elif i > sec_max_ele:
            sec_max_ele = i
    return sec_max_ele


def is_sorted(arr):
    try:
        if arr[0] > arr[1]:
            return dec(arr)
        else:
            return inc(arr)
    except IndexError:
        return 1


def inc(arr):
    cur = None
    for i in arr:
        if cur is None:
            cur = i
        elif cur > i:
            return 0
        elif cur < i:
            cur = i
    return 1


def dec(arr):
    cur = None
    for i in arr:
        if cur is None:
            cur = i
        elif cur < i:
            return 0
        elif cur > i:
            cur = i
    return 1


def get_majority(arr, x, y):
    d = {}
    for i in arr:
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1
    if d[x] > d[y]:
        return x
    elif d[x] < d[y]:
        return y
    elif d[x] == d[y]:
        if x > y:
            return y
        return x


def rotate_array(arr, n, m):
    new_array_part1 = arr[m:n:1]
    new_array_part2 = arr[0:m:1]
    return new_array_part1 + new_array_part2


def find_the_odd(arr):
    d = {}
    for i in arr:
        try:
            if d[i]:
                d[i] += 1
        except KeyError:
            d[i] = 1
    for i in d:
        if d[i] % 2 != 0:
            return i


def odd_one_using_bitwise(arr):
    # X ^ 0 = X
    # X ^ X = 0
    ans = 0
    for i in arr:
        ans = ans ^ i
    return ans


# print(sec_max([15, 12, 20, 15, 17]))
# print(rotate_array([1,2,3,4,5], 5, 3))
print(odd_one_using_bitwise([1, 1, 1, 1, 13, 2, 2, 3, 3]))












