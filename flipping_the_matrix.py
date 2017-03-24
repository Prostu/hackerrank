# Enter your code here. Read input from STDIN. Print output to STDOUT
from pprint import pprint

q = int(raw_input().strip())

for board_index in xrange(q):
    n = int(raw_input().strip())
    matrix = []
    for line in xrange(n+n):
        matrix.append(map(int, raw_input().strip().split(' ')))
    sum = 0
    for i in xrange(n):
        for j in xrange(n):
            sum += max([matrix[i][j], matrix[i][n+n-j-1], matrix[n+n-i-1][j], matrix[n+n-i-1][n+n-j-1]])
    print(sum)