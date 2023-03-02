import sys

n, m, k = map(int, input().split())
cor = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    cor[r - 1][c - 1] = 1
most = 0
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
for i in range(n):
    for j in range(m):
        if cor[i][j]:
            cor[i][j] = 0
            size = 1
            goto = {(i, j)}
            while goto:
                new_goto = set()
                for x, y in goto:
                    for k in range(4):
                        a = x + d[k][0]
                        b = y + d[k][1]
                        if cor[a][b]:
                            cor[a][b] = 0
                            size += 1
                            new_goto.add((a, b))
                goto = new_goto
            if size > most:
                most = size
print(most)
