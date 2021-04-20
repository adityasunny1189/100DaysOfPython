
# 3 Steps:

#   1. Find the base case
#   2. Assume sub-problems are solved using recursion
#   3. Using sub-problems find the correct ans


def fact(n):
    if n == 0:
        return 1
    sub_prob = fact(n-1)
    ans = n * sub_prob
    return ans


def fib(n):
    if n == 0 or n == 1:
        return 1
    sub_prob_1 = fib(n-1)
    sub_prob_2 = fib(n-2)
    ans = sub_prob_1 + sub_prob_2
    return ans


def dec(n):
    if n == 0:
        return
    print(n)
    dec(n-1)


def inc(n):
    if n == 0:
        return
    inc(n-1)
    print(n)


def sorted_array(arr):
    if len(arr) == 1:
        return True
    sub_prob = sorted_array(arr[1:])
    return arr[0] < arr[1] and sub_prob


def binary_search(arr, ele):
    if len(arr) <= 1:
        if arr[0] == ele:
            return 0
        return -1
    if arr[0] == ele:
        return 0
    sub_prob = binary_search(arr[1:], ele)
    if sub_prob >= 0:
        return sub_prob + 1
    return -1


def multiply(a, b):
    if b == 1:
        return a
    sub_prob = multiply(a, b-1)
    return a + sub_prob


def power(a: int, b: int) -> int:
    if b == 0:
        return 1
    if b == 1:
        return a
    sub_prob = power(a, b-1)
    return a * sub_prob


def first_ocr_of_key(arr: list, key: int) -> int:
    if len(arr) == 0:
        return -1
    if arr[0] == key:
        return 0
    sub_prob = first_ocr_of_key(arr[1:], key)
    if sub_prob >= 0:
        return sub_prob + 1
    return sub_prob


def last_ocr_of_key(arr: list, key: int) -> int:
    if len(arr) == 0:
        return -1
    if arr[-1] == key:
        return len(arr) - 1
    sub_prob = last_ocr_of_key(arr[0:len(arr) - 1], key)
    if sub_prob >= 0:
        return sub_prob
    return sub_prob


def print_all_index_of_key(arr: list, key: int) -> None:
    if len(arr) == 0:
        return
    print_all_index_of_key(arr[0:len(arr) - 1], key)
    if arr[len(arr) - 1] == key:
        print(len(arr) - 1)


def return_all_index_of_key(arr: list, key: int, ans_indexes: list) -> list:
    if len(arr) == 0:
        return ans_indexes
    ans_indexes = (return_all_index_of_key(arr[0:len(arr) - 1], key, ans_indexes))
    if arr[len(arr) - 1] == key:
        ans_indexes.append(len(arr) - 1)
    return ans_indexes


def fast_power_calc(a: int, n: int) -> int:
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_power_calc(a, n//2) ** 2
    return a * fast_power_calc(a, n//2) ** 2


def tower_of_hanoi(n: int, A: str, B: str, C: str) -> None:
    if n == 1:
        print(f"Move {n}th disc from {A} to {C}")
        return
    tower_of_hanoi(n-1, A, C, B)
    print(f"Move {n}th disc from {A} to {C}")
    tower_of_hanoi(n-1, B, A, C)


def josephus_problem(n: int, k: int) -> int:
    if n == 1:
        return 0
    return (josephus_problem(n-1, k) + k) % n


def remove(S):
    if len(S) == 1:
        return S
    if S[0] == S[1]:
        i = 0
        while (i + 1) < len(S) and S[i] == S[i + 1]:
            i += 1
        if (i + 1) >= (len(S)):
            return ''
        return remove(S[i+1:])
    elif S[0] != S[-1]:
        return S[0] + remove(S[1:])
    return remove(S[0] + remove(S[1:]))


def square_root(n):
    if n == 1:
        return 1
    ans = n // 2
    prev = 1
    while ans * ans > n:
        if ans * ans == n:
            return ans
        prev = ans
        ans = ans // 2

    while ans < prev:
        ans += 1
        if ans * ans < n:
            continue
        if ans * ans == n:
            return ans
        else:
            return ans - 1
    return ans


print(square_root(8))
print(square_root(6))
print(square_root(100))
print(square_root(11))












# print(remove('geeksforgeeks'))
# tower_of_hanoi(6, 'A', 'B', 'C')
# print(fast_power_calc(4,8))
# print(fast_power_calc(4,3))
# print(return_all_index_of_key([1, 2, 3, 4, 3, 2, 1], 3, []))
# print(last_ocr_of_key([1,2,3,4,3,2,1], 3))
# print(first_ocr_of_key([1,2,3,4,3,2,1], 3))
# print(power(4, 7))
# print(binary_search([1,2,3,4,5,6], 2))
# print(multiply(4, 5))
# dec(5)
# inc(5)
# print(sorted_array([1,2,3,14,5]))
# print(fib(5))
