Tcases = int(input())
while(Tcases !=0):
    Tcases -= 1

    n,k = map(int,input().split())
    s = list(input())
    count = s.count('B')
    if(count == k):
        print(0)
        continue
    print(1)
    if(count < k):
        i = 0
        while(count != k):
            if s[i] == 'A':
                count+=1
            i+=1
        print(i,'B')
    if(count > k):
        i = 0
        while(count != k):
            if s[i] == 'B':
                count-=1
            i+=1
        print(i,'A') 
