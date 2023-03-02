# 위 오른 아래 왼
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)


def dfs(x, y, cut, height):
    global cnt
    global longest
    for d in range(4):
        a, b = x + dx[d], y + dy[d]
        if not visited[a][b]:
            if mountain[a][b] < height:
                cnt += 1
                visited[x][y] = True
                dfs(a, b, cut, mountain[a][b])
                cnt -= 1
                visited[x][y] = False
            elif not cut and mountain[a][b] - k < height:
                cnt += 1
                visited[x][y] = True
                dfs(a, b, True, height - 1)
                cnt -= 1
                visited[x][y] = False
    if cnt > longest:
        longest = cnt
    return


for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    cnt = longest = 1
    mountain = [list(map(int, input().split())) + [100] for _ in range(n)] + [[100] * n]
    highest = max(mountain[i][j] for i in range(n) for j in range(n))
    visited = [[False] * n + [True] for _ in range(n)] + [[True] * n]
    for i in range(n):
        for j in range(n):
            if mountain[i][j] == highest:
                dfs(i, j, False, highest)
    print(f'#{tc}', longest)
