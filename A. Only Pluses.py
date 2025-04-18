t = int(input())
while t != 0:
    a,b,c = map(int,input().split())
    for i in range(5):
        if a <= b and a <= c:
            a = a + 1
        elif b <= c and b <= a:
            b = b + 1
        elif c <= a and c<= b:
            c = c+1
    print(a*b*c)
    t = t-1
