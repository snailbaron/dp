#!/usr/bin/env python3

x = [int(s) for s in input().split()]

s = [None] * len(x)
s[0] = [0]
for i in range(1, len(x)):
    s[i] = [i]
    for j in range(0, i):
        if x[j] < x[i] and len(s[j]) + 1 > len(s[i]):
            s[i] = s[j] + [i]

mi = 0
for i in range(0, len(x)):
    if len(s[i]) > len(s[mi]):
        mi = i
print(*[x + 1 for x in s[mi]])
