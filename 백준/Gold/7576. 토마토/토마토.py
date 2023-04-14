import sys

m, n = map(int, input().split())
storage = []
goto = set()
count = -1
for i in range(n):
    storage.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if storage[i][j] == 1:
            goto.add((i, j))
while goto:
    count += 1
    new_goto = set()
    for x, y in goto:
        storage[x][y] = -1
    for x, y in goto:
        for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= a < n and 0 <= b < m and not storage[a][b]:
                new_goto.add((a, b))
    goto = new_goto
for (i, j) in [(i, j) for i in range(n) for j in range(m)]:
    if not storage[i][j]:
        count = -1
        break
print(count)
