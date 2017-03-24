#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

def fruit_in_house(tree_position, fruit_count, fruit):
    fruit_in_house = 0
    global s, t
    for i in xrange(fruit_count):
        fruit_position = tree_position + fruit[i]
        if fruit_position >= s and fruit_position <= t:
            fruit_in_house += 1
    return fruit_in_house

print(fruit_in_house(a, m, apple))
print(fruit_in_house(b, n, orange))

