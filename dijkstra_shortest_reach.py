#!/bin/python

import sys

from heapq import heappush, heappop

t = int(raw_input().strip())
for a0 in xrange(t):
    n,m = raw_input().strip().split(' ')
    n,m = [int(n),int(m)]
    graph = [[] for i in xrange(n+1)]
    distance = [-1 for i in xrange(n+1)]    
    for edge in xrange(m):
        x,y,r = map(int, raw_input().strip().split(' '))
        graph[x].append((r, y))
        graph[y].append((r, x))
    s = int(raw_input().strip())
    distance[s] = 0
    priority_queue = []
    heappush(priority_queue, (0, s))
    while len(priority_queue) > 0:
        x_dist, x = heappop(priority_queue)
        if distance[x] < x_dist: continue
        for (r, y) in graph[x]:
            y_dist = x_dist + r
            if distance[y] == -1 or distance[y] > y_dist:
                distance[y] = y_dist
                heappush(priority_queue, (y_dist, y))
    for i in xrange(1, n+1):
        if i != s: print distance[i],
    print
