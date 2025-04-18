t = int(input())

def solve(i, n, a, c):
    # print(i, n, a)
    sol = float('inf')
    if i == n:
        return c
    if i > n:
        return -1
    for j in range(i,n):
        k = solve(j+a[j]+1,n,a,j-i)
        if k != -1:
            sol =  min(k,sol)
    sol = min(sol,n-i)

    return c + sol
    

while t != 0:
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(0, n, a,0))
    t -= 1