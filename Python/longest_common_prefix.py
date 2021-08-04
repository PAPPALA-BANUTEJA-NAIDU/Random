#!/usr/bin/python3

def lcp(strings):
    if not strings:
        return ""
    min_len = min(map(len, strings))
    i = 0
    while i < min_len:
        char = strings[0][i]
        for string in strings:
            if string[i] != char:
                return strings[0][:i]
        i += 1
    return strings[0:i]


print(lcp(["flower","flow","flight"]))
