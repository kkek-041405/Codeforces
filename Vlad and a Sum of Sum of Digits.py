t = int(input())
while t != 0:
    n = int(input())
    sum = 0
    q = int(n/9)
    if q > 0:
        sum += ((9*(9+1))/2)*q
        sum += (((q-1)*q)/2)*10
        print(q,(((q-1)*q)/2)*10) 
    else:
        sum += ((n*(n+1))/2)
    for i in range(1,q,10):
        print(i)
    print(sum)
    
    t = t-1