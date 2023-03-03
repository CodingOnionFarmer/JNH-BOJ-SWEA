make1 = {1: 0}
for x in range(2, 1000001):
    a = make1[x - 1]
    b = 99999
    c = 99999
    if not x % 2:
        b = make1[x // 2]
    if not x % 3:
        c = make1[x // 3]
    make1[x] = min(a, b, c) + 1

n = int(input())
print(make1[n])
