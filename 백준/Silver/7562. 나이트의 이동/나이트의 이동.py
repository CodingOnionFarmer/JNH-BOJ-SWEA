t = int(input())
score = {(0, 0): 0, (0, 1): 3, (0, 2): 2, (0, 3): 3, (0, 4): 2, (1, 1): 2, (1, 2): 1, (1, 3): 2, (1, 4): 3,
         (2, 2): 4, (2, 3): 3, (2, 4): 2, (3, 3): 2, (3, 4): 3, (4, 4): 4}
for _ in range(t):
    l = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    i, j = abs(a - c), abs(b - d)
    i, j = min(i, j), max(i, j)
    cnt = 0
    while j > 4:
        if i:
            i -= 1
        else:
            i = 1
        j -= 2
        if i > j:
            i, j = j, i
        cnt += 1
    corner = {(0, 0), (0, l - 1), (l - 1, 0), (l - 1, l - 1)}
    cnt += score[(i, j)]
    if (a, b) in corner or (c, d) in corner:
        if (i, j) == (1, 1):
            cnt = 4
        elif (min(abs(a - c), abs(b - d)), max(abs(a - c), abs(b - d))) == (0, 3) and l == 4:
            cnt = 5
    print(cnt)
