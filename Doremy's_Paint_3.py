Tcases = int(input())
while(Tcases !=0):
    Tcases -= 1
    n = int(input())
    a = list(input().split())
    if(len(set(a)) == 1):
        print("yes")
        continue
    if(len(set(a)) > 2):
        print("no")
        continue
    if(len(set(a)) == 2):
        temp = []
        for i in set(a):
            temp.append(a.count(i))
        if(len(a)%2 == 0 and abs(temp[0]-temp[1]) == 0):
            print("yes")
            continue
        if(len(a)%2 == 1 and abs(temp[0]-temp[1]) == 1):
            print("yes")
            continue
    print("no")

                
