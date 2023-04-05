import sys

sys.setrecursionlimit(10000)


def dfs(p, l):
    visited[p] = True
    global max_length
    if l > max_length:
        max_length = l
    for q, w in graph[p]:
        if not visited[q]:
            dfs(q, l + w)
    if l:
        visited[p] = False
    return


n = int(input())
graph = {i + 1: [] for i in range(n)}
parent = [False] * (n + 1)
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    parent[a] = True
max_length = 0
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not parent[i]:
        dfs(i, 0)
print(max_length)
