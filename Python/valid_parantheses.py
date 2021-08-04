#!/usr/bin/python3

def valid(s):
    stack = []
    open_brack = ('(', '{', '[')
    close_brack = (')', '}', ']')
    pair = dict(zip(open_brack, close_brack))

    for x in s:
        if x in open_brack:
            stack.append(pair[x])
        elif x in close_brack:
            if not stack or x != stack.pop():
                return False
    return True if not stack else False


st = input()
print(valid(st))
