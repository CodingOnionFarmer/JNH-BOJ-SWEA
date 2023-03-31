def bruteforce(size):
    for move in range(size - 1, 1, -1):
        for x in range(size - move):
            for y in range(1, size - 1):
                for left in range(max(move - (size - y - 1), 1), min(y + 1, move)):
                    right = move - left
                    path = {cafes[x][y]}
                    a, b = x, y
                    for _ in range(right):
                        a += 1
                        b += 1
                        path.add(cafes[a][b])
                    for _ in range(left):
                        a += 1
                        b -= 1
                        path.add(cafes[a][b])
                    for _ in range(right):
                        a -= 1
                        b -= 1
                        path.add(cafes[a][b])
                    for _ in range(left - 1):
                        a -= 1
                        b += 1
                        path.add(cafes[a][b])
                    if len(path) == 2 * move:
                        return 2 * move
    return -1


for tc in range(1, int(input()) + 1):
    n = int(input())
    cafes = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc}', bruteforce(n))
