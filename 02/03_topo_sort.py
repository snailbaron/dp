#!/usr/bin/env python3

n, m = [int(s) for s in input().split()]

targets = [[] for _ in range(n)]
for _ in range(m):
    u, v = [int(s) - 1 for s in input().split()]
    targets[u].append(v)

started_from = [False] * n
topo_order = []

for root in range(n):
    if not started_from[root]:
        stack = [root]
        while len(stack) > 0:
            source = stack[-1]
            if not started_from[source]:
                started_from[source] = True
                for target in targets[source]:
                    if not started_from[target]:
                        stack.append(target)
            else:
                topo_order.append(source + 1)
                stack.pop()
topo_order.reverse()

print(*topo_order)
