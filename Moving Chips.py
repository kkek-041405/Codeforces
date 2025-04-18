t = int(input())
while t!= 0:
    n = int(input())
    s = list(input().split())
    frist = True
    moves = 0
    tmov = 0
    for i in s:
        if frist and i == '1':
            frist = False
            tmov = 0
            continue
        if i == '1':
            moves+=tmov
            tmov = 0
        if i == '0':
            tmov+=1
    print(moves)
    t = t-1