move = (
    (((0, 1), (1, 0),), ((0, 1), (1, 0), (0, -1),), ((0, 1), (1, 0), (0, -1),), ((0, -1), (1, 0),),),
    (((-1, 0), (0, 1), (1, 0),), ((-1, 0), (0, 1), (1, 0), (0, -1),), ((-1, 0), (0, 1), (1, 0), (0, -1),),
     ((-1, 0), (0, -1), (1, 0),),),
    (((-1, 0), (0, 1), (1, 0),), ((-1, 0), (0, 1), (1, 0), (0, -1),), ((-1, 0), (0, 1), (1, 0), (0, -1),),
     ((-1, 0), (0, -1), (1, 0),),),
    (((0, 1), (-1, 0),), ((0, 1), (-1, 0), (0, -1),), ((0, 1), (-1, 0), (0, -1),), ((0, -1), (-1, 0),),),
)

for tc in range(1, int(input()) + 1):
    board = tuple(tuple(input().split()) for _ in range(4))
    numbers = set((board[i][j], i, j) for i in range(4) for j in range(4))
    for _ in range(6):
        make = set()
        for num, x, y in numbers:
            for dx, dy in move[x][y]:
                make.add((num + board[x + dx][y + dy], x + dx, y + dy))
        numbers = make
    print(f'#{tc}', len(set(num for num, x, y in numbers)))
