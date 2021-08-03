#/usr/bin/python3

def heapify(arr, heap_size, index):
    largest = index
    left, right = 2 * index + 1, 2 * index + 2
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, heap_size, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

if __name__ == "__main__":
    arr = [ 12, 11, 13, 5, 6, 7]
    print(*heap_sort(arr))
