t = int(input())
while t != 0:
    n = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    if s%3 == 0:
        print(0)
    elif s%3 == 2:
        print(1)
    elif s%3 == 1:
        d = False
        for i in a:
            if i%3 == 1:
                d = True
        if d:
            print(1)
        else:
            print(2)
    t = t-1
