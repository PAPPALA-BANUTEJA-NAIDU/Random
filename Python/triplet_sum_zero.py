#!/usr/bin/python3

"""
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
"""

def main(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        search_triplet(arr, -arr[i], i+1, triplets)
    return triplets


def search_triplet(arr, target, left, triplets):
    right = len(arr)-1
    while left < right:
        temp = arr[left] + arr[right]
        if temp == target:
            triplets.append([-target, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right+1]:
                right -= 1
        elif temp > target:
            right -= 1
        else:
            left += 1


print(main([-3, 3, 2, 0, 1, 2, -1, 1, -2]))
print(main([-5, 2, -1, -2, 3]))

