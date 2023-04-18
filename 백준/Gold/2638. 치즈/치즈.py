from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
hour = 0
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
while True:
    expose = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    melt = []
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny]:
                    expose[nx][ny] += 1
                    if expose[nx][ny] >= 2:
                        melt.append((nx, ny))
                elif not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    if melt:
        hour += 1
        for x, y in melt:
            board[x][y] = 0
    else:
        break
print(hour)
