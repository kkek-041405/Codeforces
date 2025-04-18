t = int(input())

while t != 0:
    String = input()
    Strings = String.split()
    ans = ""
    for i in range(len(Strings)):
        ans += Strings[i][0]
    print(ans)

    t -= 1