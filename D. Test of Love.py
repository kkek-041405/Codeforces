import time
t = int(input())
while t != 0:
    n,m,k = list(map(int,input().split()))
    a = input()
    curr = -1
    love = False
    while(curr < n):
        # print("CURR",curr,m)
        curr = curr+m
        if curr >= n: love = True;break
        flag = False
        #jumping
        for j in range(curr,curr-m,-1):
            # print('J',j)
            if(a[j] == 'L'): curr = j;flag = True;break 
        if(not flag):
            # print("no surface") 
            #JUMP + SWIMMING
            isC = False
            flag = False
            for i in range(curr,curr+k):
                print(i)
                if a[i] == 'C':
                    isC = True
                    break
                if a[i] == 'L':
                    k = k - (i + curr)
                    flag = True
                    curr = i
                    break
            if not flag:
                love = False
                break
            if isC :
                love = False
                break
    if(love):
        print("yes")
    else:
        print("NO")
    t = t-1
