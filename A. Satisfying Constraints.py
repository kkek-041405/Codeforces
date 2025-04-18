
Tcases = int(input())
while(Tcases !=0):
    Tcases -= 1

    constraits = int(input())
    l = 0
    h = 1000000000
    s = []
    for i in range(constraits):
        a,x = input().split()
        if a == '1' and int(x) > l:
            l = int(x)
        if a == '2' and int(x) < h:
            h = int(x)
        if a == '3':
            s.append(int(x))
    n = h-l
    for i in s:
        if i  <= h and i >= l:
            n -= 1
    if n < 0:
        print(0)
    else:
        print(n+1)
