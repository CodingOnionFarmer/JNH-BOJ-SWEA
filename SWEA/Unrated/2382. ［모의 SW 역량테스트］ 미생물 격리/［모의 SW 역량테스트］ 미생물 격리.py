dx = (0, -1, 1, 0, 0)
dy = (0, 0, 0, -1, 1)
turn = (0, 2, 1, 4, 3)

for tc in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    cells = {}
    for _ in range(k):
        x, y, num, d = map(int, input().split())
        cells[x, y] = num, d
    # print(cells)
    for i in range(m):
        move = {}
        check = {}
        for x, y in cells:
            num, d = cells[x, y]
            nx, ny = x + dx[d], y + dy[d]
            if 0 < nx < n - 1 and 0 < ny < n - 1:
                if (nx, ny) not in move:
                    move[nx, ny] = cells[x, y]
                elif (nx, ny) not in check:
                    check[nx, ny] = [move[nx, ny], cells[x, y]]
                else:
                    check[nx, ny].append(cells[x, y])
            else:
                num, d = cells[x, y]
                if num // 2:
                    move[nx, ny] = num // 2, turn[d]
        for section in check:
            nums = [num for (num, d) in check[section]]
            for num, d in check[section]:
                if num == max(nums):
                    move[section] = sum(nums), d
                    break
        cells = move
        # print(i, cells)
    # print(cells)
    print(f'#{tc}', sum(cells[section][0] for section in cells))
