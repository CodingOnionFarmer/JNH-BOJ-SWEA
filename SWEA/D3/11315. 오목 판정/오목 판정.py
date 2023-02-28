t = int(input())
dx = (-1, 0, 1, 1)
dy = (1, 1, 1, 0)
for tc in range(1, t + 1):
    n = int(input())
    board = [input() + '.' for _ in range(n)] + ['.' * (n + 1)]
    omok = False
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'o':
                for d in range(4):
                    x, y = i, j
                    cnt = 0
                    while board[x][y] == 'o':
                        cnt += 1
                        x += dx[d]
                        y += dy[d]
                    if cnt > 4:
                        omok = True
                        break
            if omok:
                break
        if omok:
            break
    answer = 'NO'
    if omok:
        answer = 'YES'
    print(f'#{tc}', answer)
