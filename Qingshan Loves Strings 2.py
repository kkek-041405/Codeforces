Tcases = int(input())
while(Tcases !=0):
    Tcases -= 1
    sl = int(input())
    s = input()
    c = 0
    for i in range(300):
        if s[c] == s[-c]:
            if s[c] == "1":
                print(s[:c] , "01" , s[c:],c)
                s = s[:c] + "01" + s[c:]
            elif s[c] == "0":
                S = s[::-1]
                s = s[:c] + "10" + s[c:]
                s = s[::-1]
            
            print(s)
            input()
        c +=1
        if c > len(s)/2 :
            break
            

