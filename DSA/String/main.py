s = "GeeksForGeeks"


def missing_char(string):
    d = {}
    ans = ''
    string = string.lower()
    for i in string:
        try:
            if d[i]:
                continue
        except KeyError:
            d[i] = True
    word_list = [i for i in 'abcdefghijklmnopqrstuvwxyz']
    for i in word_list:
        if i in d:
            continue
        else:
            ans += i
    if ans:
        return ans
    return -1


def palindrom_string(string):
    return string == string[::-1]


# print(missing_char('aditya'))
print(palindrom_string('baba'))
