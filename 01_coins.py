#!/usr/bin/env python3

p = [0] + [float(s) for s in input().split()]
n = len(p) - 1

old = [0.0] * (n + 1)
r = [0.0] * (n + 1)
r[0] = 1 - p[1]
r[1] = p[1]
for m in range(2, n + 1):
    old, r = r, old
    r[0] = old[0] * (1 - p[m])
    r[m] = old[m - 1] * p[m]
    for x in range(1, m):
        r[x] = old[x - 1] * p[m] + old[x] * (1 - p[m])

print(*r)
