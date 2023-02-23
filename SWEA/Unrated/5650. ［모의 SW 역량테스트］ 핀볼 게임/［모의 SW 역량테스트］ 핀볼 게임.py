t = int(input())
# 0:위 1:오른 2:아래 3:왼
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
b = [[], [2, 3, 1, 0], [1, 3, 0, 2], [3, 2, 0, 1], [2, 0, 3, 1], [2, 3, 0, 1]]

for tc in range(1, t + 1):
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())) + [5])
    board.append([5] * (n + 1))
    wormhole = {i: {} for i in range(6, 11)}
    for i in range(n):
        for j in range(n):
            if board[i][j] > 5:
                if wormhole[board[i][j]]:
                    for key in wormhole[board[i][j]]:
                        point = key
                    wormhole[board[i][j]][point] = (i, j)
                    wormhole[board[i][j]][(i, j)] = point
                else:
                    wormhole[board[i][j]] = {(i, j): (0, 0)}
    visited = [[[False] * 4 for _ in range(n)] for _ in range(n)]
    high_score = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                if not board[i][j] and not visited[i][j][k]:
                    score = 0
                    visited[i][j][k] = True
                    x = i + dx[k]
                    y = j + dy[k]
                    d = k
                    while True:
                        if x == i and y == j:
                            break
                        t = board[x][y]
                        if t == -1:
                            break
                        if not t:
                            x += dx[d]
                            y += dy[d]
                        if 0 < t < 6:
                            if (d - b[t][d]) % 4 == 2:
                                score = score * 2 + 1
                                break
                            score += 1
                            d = b[t][d]
                            x += dx[d]
                            y += dy[d]
                        if 5 < t < 11:
                            wormin = (x, y)
                            wormout = wormhole[t][wormin]
                            x = wormout[0] + dx[d]
                            y = wormout[1] + dy[d]
                    if score > high_score:
                        high_score = score
    print(f'#{tc}', high_score)