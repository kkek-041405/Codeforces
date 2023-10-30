Tcases = int(input())
while(Tcases !=0):
    Tcases -= 1
    sl,tl = input().split()
    s = input()
    t = input()
    if(sl == "1"):
        print("yes");continue
    flag = 0
    tt = True
    for i in range(int(tl)-1):
        if t[i] == t[i+1]:
            tt = False
    if(int(tl) == 1):
        tt = True
    for i in range(int(sl)-1):
        if s[i] == s[i+1]:
            if (t[-1] == s[i+1] or t[0] == s[i]) or not tt:
                flag = 1
    if flag == 1:
        print("no");continue
    print("yes")

    
