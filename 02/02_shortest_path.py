#!/usr/bin/env python3

n, m = [int(s) for s in input().split()]

targets = [[] for _ in range(n)]
for _ in range(m):
    u, v = [int(s) - 1 for s in input().split()]
    targets[u].append(v)

parent = [-1] * n

start = 0
finish = 1

queue = [start]
parent[start] = -2
while len(queue) > 0:
    source = queue.pop(0)
    if source == finish:
        break

    for target in targets[source]:
        if parent[target] == -1:
            parent[target] = source
            queue.append(target)

path = []
i = finish
while i != start:
    path.append(i + 1)
    i = parent[i]
path.append(start + 1)
path.reverse()
print(*path)
