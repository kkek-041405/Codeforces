
n = int(input())
a = input().split()
count = []
for i in a:
    for j in a:
        ticket = int(i+j)
        length = len(str(ticket))

        if(length%2 == 0):
            h1 = sum(map(int,list(str(ticket)[:int(length/2)])))
            h2 = sum(map(int,list(str(ticket)[int(length/2):])))
            if(h1 == h2):
                count.append(ticket)
print(len(count))