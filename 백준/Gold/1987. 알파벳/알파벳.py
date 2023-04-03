dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def minus65(a):
    return a - 65


def dfs(d, x, y):
    visited[board[x][y]] = True
    global max_d
    if d > max_d:
        max_d = d
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not visited[board[nx][ny]]:
            dfs(d + 1, nx, ny)
    visited[board[x][y]] = False
    return


r, c = map(int, input().split())
board = [list(map(minus65, map(ord, list(input())))) for _ in range(r)]
visited = [False] * 26
max_d = 0
dfs(1, 0, 0)
print(max_d)
