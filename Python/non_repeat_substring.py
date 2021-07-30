#!/usr/bin/python3

'''
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
'''

def main(s):
    left = 0
    ht = {}
    max_len = 0
    for right in range(len(s)):
        right_char = s[right]
        if right_char in ht:
            left = max(left, ht[right_char]+1)
        ht[right_char] = right
        max_len = max(max_len, right-left+1)
    return max_len

print(main("abccde"))
