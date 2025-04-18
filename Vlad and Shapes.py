t = int(input())
while t != 0:
    n = int(input())
    a = 0
    b = 0
    for i in range(n):
        ni = list(input())
        if ni.count('1') > 0 and a != 0 and b ==0:
            b = ni.count('1')
        if ni.count('1') > 0 and a == 0:
            a = ni.count('1')
        
        
    if abs(a - b) >= 1:
        print("TRIANGLE")
    else:
        print("SQUARE")
        

    t = t-1