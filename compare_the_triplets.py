#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
minimum = min([a,b,c,d,e])
maximum = max([a,b,c,d,e])
total = a+b+c+d+e
print("{} {}".format(total - maximum, total - minimum))