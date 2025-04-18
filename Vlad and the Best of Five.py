t = int(input())
while t != 0:
    a = list(input())
    if(a.count('A') >2):
        print('A')
    else:
        print('B')
    t = t-1