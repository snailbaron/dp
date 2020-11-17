#!/usr/bin/env python3

n, a, b, c = [int(s) for s in input().split()]

t = [0] * (n + 1)
ops = [None] * (n + 1)

t[0] = 0
ops[0] = []
for i in range(1, n + 1):
    t[i] = t[i-1] + a
    op = ops[i-1] + ["add"]
    if i % 2 == 0 and t[i//2] + b < t[i]:
        t[i] = t[i//2] + b
        op = ops[i//2] + ["double"]
    if i % 3 == 0 and t[i//3] + c < t[i]:
        t[i] = t[i//3] + c
        op = ops[i//3] + ["triple"]
    ops[i] = op

print(t[-1])
for op in ops[-1]:
    print(op)
