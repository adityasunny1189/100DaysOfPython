def groupAnagrams(s):
    do = {}
    for i in s:
        di = {}
        for j in i:
            try:
                if di[j]:
                    di[j] += 1
            except KeyError:
                di[j] = 1
        do[i] = di
    ans = []
    while len(s):
        first = s[0]
        sl = [first]
        s.remove(first)
        j = 0
        while j < len(s):
            if do[first] == do[s[j]]:
                sl.append(s[j])
                s.remove(s[j])
                continue
            j += 1
        ans.append(sl)
    return ans


print(groupAnagrams(["nyza", "anuj", "ajnu", "jydq", "yzna", "ynaz", "nuja", "njau", "jqyd", "ynza", "yqdj", "qydj"]))

print(groupAnagrams(["eat" ,"tea" ,"tan" ,"ate" , "nat" ,"bat"]))









# do = {
#     {'a': 1, 't': 1, 'e': 1}: ['ate', 'eat', 'tea'],
#     {}: []
# }


# 'ate' = {dict}
# 'tea' = {dict}

















