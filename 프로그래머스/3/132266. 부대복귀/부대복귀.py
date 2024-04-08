def solution(n, roads, sources, destination):
    answer = []
    dfd = [-1] * (n+1)  # distance from destination
    connected = [[] for _ in range(n + 1)]
    for r in range(len(roads)):
        road = roads[r]
        a,b = road[0],road[1]
        connected[a].append(b)
        connected[b].append(a)
    visited = [False] * (n + 1)
    now = {destination}
    distance = 0
    while now:
        the_next = set()
        for point in now:
            visited[point] = True
        for point in now:
            dfd[point] = distance
            for p in connected[point]:
                if not visited[p]:
                    the_next.add(p)
        distance += 1
        now = the_next
    for point in sources:
        answer.append(dfd[point])
    return answer