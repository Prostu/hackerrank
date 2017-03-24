t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    positive_sum = 0
    max_sum = a[0]
    current_sum = 0
    for x in a:
        current_sum = current_sum + x
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum =  0
        if x > 0:
            positive_sum = positive_sum + x
    if max_sum < 0:
        print(max_sum, max_sum)
    else:
        print(max_sum, positive_sum)