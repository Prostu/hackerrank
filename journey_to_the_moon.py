# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

N,l = map(int,raw_input().split())
graph = [[] for i in xrange(N)]
visited = [False for i in xrange(N)]

for i in xrange(l):
    a,b = map(int,raw_input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(node):
    global visited, graph
    component_size = 0
    visited[node] = 1
    queue = deque([node])
    while len(queue) > 0:
        node = queue.popleft()
        component_size += 1
        for addiacent in graph[node]:
            if not visited[addiacent]:
                visited[addiacent] = True
                queue.append(addiacent)
    return component_size
    
result = 0
partial = 0
for node in xrange(N):
    if not visited[node]:
        component_size = bfs(node)
        result += partial * component_size
        partial += component_size
        
print result
