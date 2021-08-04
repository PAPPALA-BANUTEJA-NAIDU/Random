#!/usr/bin/python3

def remove_duplicates(arr):
    i, next_non_duplicate = 1, 1
    while i < len(arr):
        if arr[next_non_duplicate-1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate, arr[:next_non_duplicate]


print(remove_duplicates([2, 2, 3, 3, 5, 5, 7, 11]))
