t = int(input())
while t != 0:
    n, m = list(map(int, input().split()))
    a = list(input())
    b = list(input())
    output = 0
    i = 0
    for j in range(len(a)):
        temp = output
        for k in range(i,len(b)):
            if b[k] == a[j]:
                i = k+1
                output += 1
                break
        if temp == output:
            break
    print(output)
    t-=1
