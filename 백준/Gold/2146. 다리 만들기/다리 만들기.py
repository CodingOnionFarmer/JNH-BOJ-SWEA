import sys

n = int(input())
imap = []
visited = [[False] * n for _ in range(n)]
for i in range(n):
    imap.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if not imap[i][j]:
            visited[i][j] = True
islands = []
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            goto = {(i, j)}
            group = set()
            while True:
                for x, y in goto:
                    visited[x][y] = True
                    group.add((x, y))
                new_goto = set()
                for x, y in goto:
                    for a, b in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                        if 0 <= a < n and 0 <= b < n and not visited[a][b]:
                            new_goto.add((a, b))
                goto = new_goto
                if not goto:
                    break
            islands.append(group)
shortest = 2001
for island in islands[:-1]:
    visited = [[False] * n for _ in range(n)]
    goto = island
    cnt = -1
    for x, y in island:
        imap[x][y] = 0
    arrived = False
    while True:
        for x, y in goto:
            visited[x][y] = True
            if imap[x][y]:
                arrived = True
                break
        if arrived:
            break
        new_goto = set()
        for x, y in goto:
            for a, b in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                if 0 <= a < n and 0 <= b < n and not visited[a][b]:
                    new_goto.add((a, b))
        goto = new_goto
        cnt += 1
    if cnt < shortest:
        shortest = cnt
print(shortest)
