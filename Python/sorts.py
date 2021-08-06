#!/usr/bin/python3

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i):
            if arr[i] < arr[j]:
                arr.insert(j, arr[i])
                arr.pop(i+1)
                break
    return arr

def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr)//2 :])
    return merge(left, right)


print(bubble_sort([5,2,7,5, 4, 9,1]))
print(selection_sort([5,2,7,5, 4, 9,1]))
print(insertion_sort([5,2,7,5, 4, 9,1]))
print(merge_sort([5,2,7,5, 4, 9,1]))
print(quick_sort([5,2,7,5, 4, 9,1]))

