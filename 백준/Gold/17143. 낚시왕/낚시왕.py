import sys

R, C, M = map(int, input().split())
sea = [[None] * C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    if d < 3:
        s %= 2 * R - 2
        if d == 1:
            s = 2 * R - 2 - s
    else:
        s %= 2 * C - 2
        if d == 4:
            s = 2 * C - 2 - s
        d = 0
    sea[r - 1][c - 1] = (r - 1, c - 1, s, d, z)
position = -1
caught = 0

for _ in range(C):
    position += 1
    for i in range(R):
        if sea[i][position]:
            caught += sea[i][position][4]
            sea[i][position] = None
            break
    move = [[None] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if sea[i][j]:
                r, c, s, d, z = sea[i][j]
                if d:
                    r += s
                    r %= 2 * R - 2
                    i1 = r
                    if i1 >= R:
                        i1 = 2 * R - 2 - i1
                    if move[i1][j]:
                        r1, c1, s1, d1, z1 = move[i1][j]
                        if z1 > z:
                            r, c, s, d, z = r1, c1, s1, d1, z1
                    move[i1][j] = (r, c, s, d, z)
                else:
                    c += s
                    c %= 2 * C - 2
                    j = c
                    if j >= C:
                        j = 2 * C - 2 - c
                    if move[i][j]:
                        r1, c1, s1, d1, z1 = move[i][j]
                        if z1 > z:
                            r, c, s, d, z = r1, c1, s1, d1, z1
                    move[i][j] = (r, c, s, d, z)
    sea = move
print(caught)
