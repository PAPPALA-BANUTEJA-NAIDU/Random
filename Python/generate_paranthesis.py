#!/usr/bin/python3

def generate_paranthesis(n):
    result = []
    current = ''
    generate_recursive(n, n, current, result)
    return result


def generate_recursive(left, right, current, result):
    if left == 0 and right == 0:
        result.append(current)
    if left > 0:
        generate_recursive(left-1, right, current+'(', result)
    if left < right:
        generate_recursive(left, right-1, current+')', result)

n = int(input())
print(generate_paranthesis(n))

