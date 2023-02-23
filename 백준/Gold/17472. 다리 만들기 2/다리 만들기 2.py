import sys

n, m = map(int, input().split())
imap = []
visited = [[False] * m for _ in range(n)]
for i in range(n):
    imap.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if not imap[i][j]:
            visited[i][j] = True
islands = []
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            goto = {(i, j)}
            group = set()
            while goto:
                for x, y in goto:
                    visited[x][y] = True
                    group.add((x, y))
                new_goto = set()
                for x, y in goto:
                    for a, b in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                        if 0 <= a < n and 0 <= b < m and not visited[a][b]:
                            new_goto.add((a, b))
                goto = new_goto
            islands.append(group)
ic = len(islands)
bridge = {(i, j): 100 for i in range(ic) for j in range(ic)}
for x in range(n):
    start = False
    cnt = 0
    for y in range(m):
        if imap[x][y]:
            if not cnt:
                start = True
                start_from = y
            else:
                for i in range(ic):
                    if (x, start_from) in islands[i]:
                        b1 = i
                    if (x, y) in islands[i]:
                        b2 = i
                if 1 < cnt < bridge[(b1, b2)]:
                    bridge[(b1, b2)] = bridge[(b2, b1)] = cnt
                cnt = 0
                start_from = y
        else:
            if start:
                cnt += 1
for y in range(m):
    start = False
    cnt = 0
    for x in range(n):
        if imap[x][y]:
            if not cnt:
                start = True
                start_from = x
            else:
                for i in range(ic):
                    if (start_from, y) in islands[i]:
                        b1 = i
                    if (x, y) in islands[i]:
                        b2 = i
                if 1 < cnt < bridge[(b1, b2)]:
                    bridge[(b1, b2)] = bridge[(b2, b1)] = cnt
                cnt = 0
                start_from = x
        else:
            if start:
                cnt += 1
real_bridge = {}
can_go = []
for i in range(ic - 1):
    for j in range(i + 1, ic):
        if bridge[(i, j)] < 100:
            can_go.append((i, j))
            real_bridge[(i, j)] = bridge[(i, j)]
least = 100
cnt = 0
distance = 0
para = -1
graph = {i: set() for i in range(ic)}


def dfs():
    global cnt
    global distance
    if cnt == ic - 1:
        visited = set()
        goto = {0}
        while goto:
            for x in goto:
                visited.add(x)
            new_goto = set()
            for x in goto:
                for y in graph[x]:
                    if y not in visited:
                        new_goto.add(y)
            goto = new_goto
        if len(visited) == ic:
            global least
            if distance < least:
                least = distance
        return
    global para
    fix = para
    for i in range(para + 1, len(can_go)):
        x, y = can_go[i]
        graph[x].add(y)
        graph[y].add(x)
        distance += real_bridge[(x, y)]
        cnt += 1
        para = i
        dfs()
        para = fix
        cnt -= 1
        distance -= real_bridge[(x, y)]
        graph[x].remove(y)
        graph[y].remove(x)
    return


dfs()
if least == 100:
    least = -1
print(least)
