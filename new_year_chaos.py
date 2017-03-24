#!/bin/python

import sys
from pprint import pprint

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    v = range(1, n+1)
    bribes = 0
    chaotic = False
    # your code goes here
    for i in xrange(n):
        if q[i] == v[i]:
            continue
        if i + 1 < n and q[i] == v[i+1]:
            bribes += 1
            v[i+1] = v[i]
            v[i] = q[i]
            continue
        if i + 2 < n and q[i] == v[i+2]:
            bribes += 2
            v[i+2] = v[i+1]
            v[i+1] = v[i]
            v[i] = q[i]
            continue
        chaotic = True
        break;
    if chaotic:
        print("Too chaotic")
    else:
        print(bribes)
