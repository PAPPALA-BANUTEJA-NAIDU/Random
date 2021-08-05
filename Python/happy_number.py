#!/usr/bin/python3

"""
Any number will be called a happy number if, 
after repeatedly replacing it with a number equal to the sum of the square of all of its digits, 
leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. 
Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
"""


def happy(num):
    fast, slow = num, num
    while True:
        fast = square(square(fast))
        slow = square(slow)
        if fast == slow:
            break
    return slow == 1

def square(num):
    digit_sum = 0
    while num > 0:
        digit_sum += (num%10) ** 2
        num = num // 10
    return digit_sum

print(happy(23))
print(happy(12))

