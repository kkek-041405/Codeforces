Tcases = int(input())
while(Tcases !=0):
    Tcases -= 1

    n,k,x = list(map(int,input().split()))
    a = list(map(int,input().split()))
    a.sort()
    s = 0
    
    
    s = sum(a[:n-x]) - sum(a[n-x:])
    
    print(s)
    
    