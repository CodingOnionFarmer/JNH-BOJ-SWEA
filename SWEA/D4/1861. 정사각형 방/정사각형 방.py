dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

for tc in range(1, int(input()) + 1):
    n = int(input())
    rooms = [list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * n]
    check = [False] * n ** 2
    for i in range(n):
        for j in range(n):
            num = rooms[i][j]
            for k in range(4):
                if rooms[i + dx[k]][j + dy[k]] == num + 1:
                    check[num] = True
                    break
    start = 1
    max_move = 1
    move = 1
    for i in range(n ** 2):
        if check[i]:
            move += 1
            if move > max_move:
                start = i + 2 - move
                max_move = move
        else:
            move = 1
    print(f'#{tc}', start, max_move)
