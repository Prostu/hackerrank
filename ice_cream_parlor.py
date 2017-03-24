# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input().strip())
for test_i in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    c = map(int, raw_input().strip().split(' '))
    hash = {}
    for i, v in enumerate(c): 
        if m - v in hash:
            print("{} {}".format(hash[m-v]+1, i+1))
            break
        hash[v] = i
