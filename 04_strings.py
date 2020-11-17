#!/usr/bin/env python3

import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

s = [[""] * (len(b) + 2) for i in range(len(a) + 2)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            s[i][j] = s[i-1][j-1] + a[i-1]
        else:
            if len(s[i-1][j]) >= len(s[i][j-1]):
                s[i][j] = s[i-1][j]
            else:
                s[i][j] = s[i][j-1]

print(s[len(a)][len(b)])
