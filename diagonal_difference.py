#!/bin/python

import sys
from pprint import pprint


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
first_diagonal_sum = sum([a[a_i][a_i] for a_i in xrange(n)])
second_diagonal_sum = sum([a[a_i][n-a_i-1] for a_i in xrange(n)])
print(abs(first_diagonal_sum - second_diagonal_sum))