#!/usr/bin/env python3

import sys

t = [int(s) for s in input().split()]

if len(t) == 1:
    print(t[0])
    sys.exit(0)
elif len(t) <= 4:
    print(t[0] + t[-1])
    sys.exit(0)

s = [0] * len(t)
l = [None] * len(t)

s[0] = t[0]
s[1] = t[0] + t[1]
s[2] = t[0] + t[2]
s[3] = t[0] + t[3]

l[0] = [0]
l[1] = [0, 1]
l[2] = [0, 2]
l[3] = [0, 3]

for i in range(4, len(t)):
    m = min(s[i-3], s[i-2], s[i-1])
    if m == s[i-3]:
        l[i] = l[i-3] + [i]
    elif m == s[i-2]:
        l[i] = l[i-2] + [i]
    else:
        l[i] = l[i-1] + [i]
    s[i] = m + t[i]

print(*[x + 1 for x in l[-1]])
