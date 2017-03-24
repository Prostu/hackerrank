# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque   

q = int(raw_input())
for q_i in xrange(q):
    n, m = map(int, raw_input().strip().split(' '))
    graph = [[] for i in xrange(n+1)]
    for m_i in xrange(m):
        u, v = map(int, raw_input().strip().split(' '))
        graph[u].append(v)
        graph[v].append(u)
    s = int(raw_input())
    
    dist = [-1 for i in xrange(n+1)]
    dist[s] = 0
    queue = deque()
    queue.append(s)
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 6
                queue.append(v)
    for i in xrange(1, n+1):
        if i != s:
            print dist[i],
    print ''