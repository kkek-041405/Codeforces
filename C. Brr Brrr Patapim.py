t = int(input())

while t != 0:
    t -= 1
    n = int(input())
    g = [input().split() for x in range(n)]
    # print(g)
    ans = []
    for i in range(n+n):
        ans.append(0)
    # print(ans)
    for i in range(len(g)):
        for j in range(len(g[i])):
            if i+j+1 < len(ans):
                ans[i+j+1] = int(g[i][j])

    for i in range(n+n+1):
        # print(i not in ans,i, end=" ")
        if i not in ans:
            ans[0] = i


    for i in range(len(ans)):
        print(ans[i], end=" ")
    print()

