n, m, d = map(int, input().split())
cd = [list(map(int, input().split())) for _ in range(n)]
most_killed = 0


def shoot(r, c):
    for di in range(d):
        for cdi in range(-di, di + 1):
            x, y = n - 1 - r - di + abs(cdi), c + cdi
            if 0 <= x and 0 <= y < m and cd[x][y] and (x, y) not in killed:
                return x, y
    return


for i in range(0, m - 2):
    for j in range(i + 1, m - 1):
        for k in range(j + 1, m):
            killed = set()
            for r in range(n):
                kill = set()
                for l in (i, j, k):
                    s = shoot(r, l)
                    if s:
                        kill.add(s)
                killed |= kill
            if len(killed) > most_killed:
                most_killed = len(killed)
print(most_killed)
