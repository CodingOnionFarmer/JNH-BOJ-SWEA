import sys, heapq

n, m, x = map(int, input().split())
back = [[] for _ in range(n + 1)]
go = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    back[u].append((v, t))
    go[v].append((u, t))
dist1 = [100000] * (n + 1)
dist2 = [100000] * (n + 1)


def dijkstra_go(start):
    q = []
    dist1[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if dist1[now] < d:
            continue
        for i in go[now]:
            cost = d + i[1]
            if cost < dist1[i[0]]:
                dist1[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


def dijkstra_back(start):
    q = []
    dist2[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if dist2[now] < d:
            continue
        for i in back[now]:
            cost = d + i[1]
            if cost < dist2[i[0]]:
                dist2[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra_go(x)
dijkstra_back(x)
print(max(dist1[i] + dist2[i] for i in range(1, n + 1)))
