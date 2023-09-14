import sys

input = sys.stdin.readline
inf = 1e9
l, p = map(int, input().split())
fun = [int(input()) for _ in range(l)]
road = {i: set() for i in range(l)}
for i in range(p):
    l1, l2, t = map(int, input().split())
    road[l1 - 1].add((l2 - 1, t))
best = 0
graph = [[inf, 0, []] for _ in range(l)]  # 시간, 재미, 경로
graph[0][0] = 0
graph[0][1] = fun[0]
graph[0][2].append(0)
for i in range(l):
    for j in range(l):
        if graph[j][0] < inf:
            for k, t in road[j]:
                if len(graph[j][2]) > len(graph[k][2]) and graph[j][2][len(graph[k][2]) - 1] == k:
                    fpt = (graph[j][1] - graph[k][1] + fun[k]) / (graph[j][0] - graph[k][0] + t)
                    # print('사이클 확인')
                    # print(j, k, graph[j][2], fpt)
                    if fpt > best:
                        best = fpt
                else:
                    if (graph[j][1] + fun[k]) * graph[k][0] > graph[k][1] * (graph[j][0] + t):
                        graph[k][0] = graph[j][0] + t
                        graph[k][1] = graph[j][1] + fun[k]
                        graph[k][2] = graph[j][2] + [k]
# print(graph)
if best:
    print(format(round(best, 2), '.2f'))
else:
    print(0)
