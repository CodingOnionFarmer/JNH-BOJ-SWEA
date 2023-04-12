import sys, heapq

INF = 2400000
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
dist = [INF] * (n + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


v1v2 = 0
v2v1 = 0
dijkstra(1)
v1v2 += dist[v1]
v2v1 += dist[v2]
dist = [INF] * (n + 1)
dijkstra(v1)
v1v2 += dist[v2]
v2v1 += dist[n]
dist = [INF] * (n + 1)
dijkstra(v2)
v1v2 += dist[n]
v2v1 += dist[v1]
if v1v2 >= INF and v2v1 >= INF:
    print(-1)
else:
    print(min(v1v2, v2v1))
