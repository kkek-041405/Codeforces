t = int(input())
while t != 0:
    s = input()
    r = input()

    sl = 0
    rl = 0
    pos = True
    while rl < len(r) and sl < len(s):
        print(rl,sl)
        while  sl+1 < len(s) and s[sl] == r[rl]:
            sl += 1
        while rl+1 < len(r) and r[rl] != s[sl]:
            rl += 1
        if (rl < sl) or (rl > 2*sl):
            pos = False
            break
    
    if pos:
        print("YES")
    else: print("NO")

