t = int(input())
while t != 0:
    n = int(input())
    a = list(map(int,input().split()))
    sum = 0
    for i in a:
        if i > 0: sum += i
        else: sum -= i
    print(sum)
    t = t-1