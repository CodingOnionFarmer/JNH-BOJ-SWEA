import sys

r, c, t = map(int, input().split())
room = [list(map(int, sys.stdin.readline().split())) + [-1] for _ in range(r)] + [[-1] * c]
for i in range(r):
    if room[i][0] == -1:
        ac = i
for _ in range(t):
    change = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] > 4:
                cnt = 0
                dif = room[i][j] // 5
                for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    if room[x][y] != -1:
                        change[x][y] += dif
                        cnt += 1
                change[i][j] -= cnt * dif
    for i in range(r):
        for j in range(c):
            room[i][j] += change[i][j]
    for i in range(ac - 2):
        room[ac - 2 - i][0] = room[ac - 3 - i][0]
    for i in range(r - ac - 2):
        room[ac + 1 + i][0] = room[ac + 2 + i][0]
    for j in range(c - 1):
        room[0][j] = room[0][j + 1]
        room[r - 1][j] = room[r - 1][j + 1]
    for i in range(ac - 1):
        room[i][c - 1] = room[i + 1][c - 1]
    for i in range(r - ac - 1):
        room[r - 1 - i][c - 1] = room[r - 2 - i][c - 1]
    for j in range(c - 2):
        room[ac - 1][c - 1 - j] = room[ac - 1][c - 2 - j]
        room[ac][c - 1 - j] = room[ac][c - 2 - j]
    room[ac - 1][1] = room[ac][1] = 0
print(sum([sum(line) for line in room]) + 2 + r + c)
