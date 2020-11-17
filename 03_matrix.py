#!/usr/bin/env python3

import sys

a = []
for line in sys.stdin:
    line = line.rstrip()
    a.append([int(x) for x in line.split()])
n = len(a)
m = len(a[0])

for i in range(1, n):
    a[i][0] += a[i - 1][0]
for j in range(1, m):
    a[0][j] += a[0][j - 1]
for i in range(1, n):
    for j in range(1, m):
        a[i][j] += min(a[i - 1][j], a[i][j - 1])

print(a[n - 1][m - 1])
