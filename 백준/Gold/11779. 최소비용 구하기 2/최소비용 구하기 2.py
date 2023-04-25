import sys, heapq

input = sys.stdin.readline
n, m = int(input()), int(input())
bus = [{} for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if b not in bus[a] or bus[a][b] > c:
        bus[a][b] = c
s, e = map(int, input().split())
INF = 10 ** 8
distance = [INF] * (n + 1)
before = [0] * (n + 1)


def dijkstra(start):
    distance[start] = 0
    q = [(0, start)]
    while q:
        dist, now = heapq.heappop(q)
        for go in bus[now]:
            if dist + bus[now][go] >= distance[go]:
                continue
            distance[go] = dist + bus[now][go]
            before[go] = now
            heapq.heappush(q, (dist + bus[now][go], go))


dijkstra(s)
path = [e]
backtrack = e
while before[backtrack]:
    backtrack = before[backtrack]
    path.append(backtrack)
print(distance[e])
print(len(path))
print(*reversed(path))
