t = int(input())
while t != 0:
    n,k = list(map(int,input().split()))
    a   = list(map(int,input().split()))
    x   = list(map(int,input().split()))

    e = {}
    for i in range(n):
        if not (e.keys()).__contains__(abs(x[i])):
            e.update({abs(x[i]):a[i]})
        else:
            e.update({abs(x[i]):a[i]+e.get(abs(x[i]))})
        
    for i in range(n,0,-1):
        if (e.keys()).__contains__(i):
            for j in range(i-1,0,-1):
                if (e.keys()).__contains__(j):
                    e.update({i:e.get(i)+e.get(j)})
            
    p = True
    for key in  e.keys():
        if e.get(key) > k*key:
            p = False
    if p:
        print("yes")
    else:
        print("no")
        
    t=t-1