#!/usr/bin/python3

from collections import deque

def dfs(G, s):
    visited, traversal_stack = {s}, [s]
    print(s)
    while traversal_stack:
        flag = 0
        for i in G[traversal_stack[-1]]:
            if i not in visited:
                traversal_stack.append(i)
                visited.add(i)
                flag = 1
                print(i)
                break
        if not flag:
            traversal_stack.pop()


def bfs(G, s):
    visited, queue = {s}, deque([s])
    print(s)
    while queue:
        x = queue.popleft()
        for i in G[x]:
            visited.add(i)
            queue.append(i)
            print(i)


