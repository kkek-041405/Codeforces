Tcases = int(input())
while(Tcases !=0):
    Tcases -= 1
    n,m = [int(x) for x in input().split()]
    if(n%m == 0):
        print(0)
        continue
    if(m == n):
        print(n)
        continue
    if(m%2 == 1):
        print("-1")
        continue
    op = 0
    while(n%m != 0):
        ch = n%m
        n += ch
        op += ch
        print(n%m)
        print(n/m)
        print(op)