n = int(input())
sea = [list(map(int, input().split())) + [30] for _ in range(n)]
sea.append([30] * n)
size = 2
ate = 0
move = 0
d = {(0, 1), (0, -1), (1, 0), (-1, 0)}
fish = {i: 0 for i in range(1, 7)}
p = q = 0
for i in range(n):
    for j in range(n):
        if 0 < sea[i][j] < 7:
            fish[sea[i][j]] += 1
        if sea[i][j] == 9:
            p, q = i, j
            sea[i][j] = 0
while True:
    visited = {(p, q)}
    can_eat = set()
    goto = {(p, q)}
    step = 0
    while not can_eat and goto:
        new_goto = set()
        for x, y in goto:
            for dx, dy in d:
                if (x + dx, y + dy) not in visited:
                    visited.add((x + dx, y + dy))
                    if sea[x + dx][y + dy] <= size:
                        new_goto.add((x + dx, y + dy))
                        visited.add((x + dx, y + dy))
                        if size > sea[x + dx][y + dy] > 0:
                            can_eat.add((x + dx, y + dy))
        goto = new_goto
        step += 1
    if not can_eat:
        break
    p, q = sorted(list(can_eat))[0]
    sea[p][q] = 0
    ate += 1
    move += step
    if ate == size:
        ate = 0
        size += 1
print(move)
