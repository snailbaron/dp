#!/usr/bin/env python3

x = [int(s) for s in input().split()]

s = [0] * len(x)
for i in range(len(x)):
    s[i] = 1
    for j in range(i):
        if x[j] < x[i] and s[j] + 1 > s[i]:
            s[i] = s[j] + 1
print(max(s))
