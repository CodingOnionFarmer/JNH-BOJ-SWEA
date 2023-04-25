import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

v = int(input())
graph = [list(map(int, input().split())) for _ in range(v)]
graph.sort()
if v == 2:
    print(graph[0][2])
else:
    diameter = 0
    distance = [{} for _ in range(v)]
    # checked = [False] * v


    def dfs(p, bp):
        # checked[p] = True
        dist1 = dist2 = 0
        for i in range(len(graph[p]) // 2 - 1):
            np = graph[p][i * 2 + 1] - 1
            if np == bp:
                continue
            if len(graph[np]) == 4:
                distance[p][np] = graph[p][i * 2 + 2]
            # elif checked[np]:
            #     distance[p][np] = graph[p][i * 2 + 2] + max(distance[np][j] for j in distance[np] if j != p)
            else:
                dfs(np, p)
                distance[p][np] = graph[p][i * 2 + 2] + max(distance[np].values())
            if distance[p][np] > dist1:
                dist1, dist2 = distance[p][np], dist1
            elif distance[p][np] > dist2:
                dist2 = distance[p][np]
        global diameter
        if dist1 + dist2 > diameter:
            diameter = dist1 + dist2


    for n in range(v):
        if len(graph[n]) > 4:
            dfs(n, n)
            break
    # print(distance)
    print(diameter)
