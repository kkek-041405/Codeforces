t = int(input())
while t!=0:
    n  = int(input())
    a  = list(map(int,input().split()))
    a.sort(reverse=True)
    p = True
    m = a[0]
    for i in range(1,n):
        if m%a[i] == 0:
            p = False
        print(m%a[i])
        m = m%a[i]
    if p:
        print('yes')
    else:
        print('no')

    
    t = t - 1