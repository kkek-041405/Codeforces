t = int(input())
while t != 0:
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    sum = 0
    a.pop(a.index(max(a)))
    for i in a:
        if i == 1:
            sum += 1
            continue
        sum += 1
        sum += (i-1)*2
    print(sum)
    t = t-1
