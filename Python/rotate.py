#!/usr/bin/python3

def rotate(string, k):
    long = (string) * (k // len(string) + 2)
    if k <= len(string):
        return long[k: k + len(string)]
    else:
        return long[k-len(string):k]

def rotate_alt(string, k):
    k = k % len(string)
    return string[k : ] + string[:k]

print(rotate("hello", 2))
print(rotate("hello", 2))
print(rotate("hello", 6))
print(rotate("hello", 50))
print(rotate_alt("hello", 1002))
print(rotate_alt("hello", 6))
print(rotate_alt("hello", 50))
print(rotate_alt("hello", 1002))
