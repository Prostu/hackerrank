# Enter your code here. Read input from STDIN. Print output to STDOUT

s = raw_input().strip()
while True:
    reduced_s = []
    i = 0
    while i < len(s):
        if i+1 < len(s) and s[i] == s[i+1]:
            i += 2
        else:
            reduced_s.append(s[i])
            i += 1
    updated_s = ''.join(reduced_s)
    if updated_s == s:
        break
    else:
        s = updated_s

if len(s) == 0:
    print("Empty String")
else:
    print(s)