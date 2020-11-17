#!/usr/bin/env python3

years = [int(s) for s in input().split()]

l = [0] * len(years)
for i in range(len(years)):
    l[i] = 1
    for j in range(i):
        if years[j] <= years[i] and l[j] + 1 > l[i]:
            l[i] = l[j] + 1
print(len(years) - max(l))
