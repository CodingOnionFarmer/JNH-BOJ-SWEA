import sys

n, m, v = map(int, input().split())
visited = [False] * (n + 1)
connected = {i + 1: [] for i in range(n)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    connected[a].append(b)
    connected[b].append(a)
for i in range(n):
    connected[i + 1].sort()


def dfs(v):
    global visited
    print(v, end=' ')
    visited[v] = True
    for i in connected[v]:
        if not visited[i]:
            dfs(i)


def bfs(lst):
    global visited
    if not len(lst):
        return
    if not visited[lst[0]]:
        print(lst[0], end=' ')
        visited[lst[0]] = True
    next = []
    for v in lst:
        for i in connected[v]:
            if not visited[i]:
                visited[i] = True
                print(i, end=' ')
                next.append(i)
    bfs(next)


dfs(v)
print()
visited = [False] * (n + 1)
bfs([v])
