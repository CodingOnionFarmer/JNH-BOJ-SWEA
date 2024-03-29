import heapq, sys

input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
INF = 200000
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)
visited = [False] * (V + 1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
q = []
heapq.heappush(q, (0, k))
distance[k] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
