# Enter your code here. Read input from STDIN. Print output to STDOUT

V = int(raw_input().strip())
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

p = 1
while (p << 1) <= n: 
    p <<= 1
i = 0
while p > 0:
    t = i + p
    if t < n and arr[t] <= V:
        i = t
    p >>= 1
print(i)