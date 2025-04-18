t = int(input())


def find_array(x):
  a = [999999998-sum(x)]
  for i in range(len(x)):
    a = a + [a[-1]+x[i]]
    # print(a[-1]%a[-2])
  return a


for _ in range(t):
  n = int(input())
  x = list(map(int, input().split()))
  a = find_array(x)
  print(*a)
