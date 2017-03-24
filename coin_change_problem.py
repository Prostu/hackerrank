from pprint import pprint

[n, m] = map(int,raw_input().strip().split(' '))
arr = map(int,raw_input().strip().split(' '))
D = [0 for x in xrange(n+1)]
D[0] = 1
for j in xrange(m):
    for i in xrange(arr[j], n+1):
        D[i] += D[i-arr[j]]
            
print(D[n])