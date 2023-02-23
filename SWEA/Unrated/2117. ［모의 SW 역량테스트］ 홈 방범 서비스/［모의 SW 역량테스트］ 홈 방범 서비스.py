t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    house = []
    for i in range(n):
        for j in range(n):
            if city[i][j]:
                house.append((i, j))
    k = n // 2 * 2 + 1
    if len(house) * m >= k ** 2 + (k - 1) ** 2:
        print(f'#{tc}', len(house))
    else:
        k -= 1
        cr = (n // 2 - 1, (n + 1) // 2 + 1)
        found = False
        most = 0
        while True:
            for i in range(cr[0], cr[1]):
                for j in range(cr[0], cr[1]):
                    center = (i, j)
                    secure = [(x, y) for x, y in house if abs(x - i) + abs(y - j) < k]
                    if len(secure) * m >= k ** 2 + (k - 1) ** 2:
                        found = True
                        if len(secure) > most:
                            most = len(secure)
            if found:
                break
            k -= 1
            if not k % 2:
                cr = (cr[0] - 1, cr[1] + 1)
        print(f'#{tc}', most)
