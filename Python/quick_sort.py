#!/usr/bin/python3

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [int(x) for x in arr[1:] if x <= pivot]
        right = [int(x) for x in arr[1:] if x > pivot]

        return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([10, 5, 2, 3]))

