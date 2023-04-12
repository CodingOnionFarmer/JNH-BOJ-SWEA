n = int(input())
board = [[' '] * (n * 2 - 1) for _ in range(n)]


# x,y는 상단 꼭짓점의 좌표
def sierpinski(size, x, y):
    if size == 3:
        board[x][y] = board[x + 1][y - 1] = board[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            board[x + 2][y + i] = '*'
        return
    size //= 2
    sierpinski(size, x, y)
    sierpinski(size, x + size, y - size)
    sierpinski(size, x + size, y + size)
    return


sierpinski(n, 0, n - 1)
for line in board:
    print(*line, sep='')
