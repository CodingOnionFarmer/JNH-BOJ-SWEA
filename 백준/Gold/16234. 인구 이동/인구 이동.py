import sys

n, l, r = map(int, input().split())
countries = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0
while True:
    visited = [[False] * n for _ in range(n)]
    groups = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                goto = {(a, b) for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)] if
                        0 <= a < n and 0 <= b < n and not visited[a][b] and l <= abs(
                            countries[a][b] - countries[i][j]) <= r}
                group = {(i, j)}
                for x, y in goto:
                    visited[x][y] = True
                while goto:
                    for x, y in goto:
                        group.add((x, y))
                    new_goto = set()
                    for x, y in goto:
                        for a, b in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                            if 0 <= a < n and 0 <= b < n and not visited[a][b] and l <= abs(
                                    countries[a][b] - countries[x][y]) <= r:
                                new_goto.add((a, b))
                                visited[a][b] = True
                    goto = new_goto
                if len(group) > 1:
                    groups.append(group)
    if groups:
        cnt += 1
        for group in groups:
            av = sum(countries[a][b] for (a, b) in group) // len(group)
            for (a, b) in group:
                countries[a][b] = av
    else:
        break
print(cnt)
