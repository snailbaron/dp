#!/usr/bin/env python3

n, m = [int(s) for s in input().split()]

targets = [[] for _ in range(n)]
for _ in range(m):
    u, v = [int(s) - 1 for s in input().split()]
    targets[u].append(v)
    targets[v].append(u)

seen = [False] * n

for root in range(n):
    if not seen[root]:
        component = [root + 1]
        seen[root] = True
        stack = [root]
        while len(stack) > 0:
            source = stack.pop()
            for target in targets[source]:
                if not seen[target]:
                    seen[target] = True
                    stack.append(target)
                    component.append(target + 1)
        print(*component)
