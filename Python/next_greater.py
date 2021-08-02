#!/usr/bin/python3

def next_greater(arr):
    s = []
    for i in range(len(arr)):
        while s and s[-1].get("value") < arr[i]:
            d = s.pop()
            arr[d.get("index")] = arr[i]
        s.append({"value": arr[i], "index": i})
    while s:
        d = s.pop()
        arr[d.get("index")] = -1
    return arr

print(next_greater([6,8,0,1,3]))

