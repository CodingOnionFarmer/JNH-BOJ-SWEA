seat = [input() for _ in range(5)]
connected = {(i, j): set() for i in range(5) for j in range(5)}
seat_num = {i: (i // 5, i % 5) for i in range(25)}
for i in range(5):
    for j in range(5):
        connected[i * 5 + j] = set()
for i in range(5):
    for j in range(5):
        seat_num[(i, j)] = i * 5 + j
        for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < 5 and 0 <= y < 5:
                connected[(i, j)].add((x, y))
                connected[(x, y)].add((i, j))
                connected[i * 5 + j].add(x * 5 + y)
                connected[x * 5 + y].add(i * 5 + j)

seats = set()
c = 0


def check(seats7):
    for i in seats7:
        goto = {i}
        visited = set()
        while goto:
            new_goto = set()
            for j in goto:
                visited.add(j)
            for j in goto:
                for k in connected[j]:
                    if k in seats7 and k not in visited:
                        new_goto.add(k)
            goto = new_goto
        if len(visited) == 7:
            cnt = 0
            for m in visited:
                p, q = seat_num[m]
                if seat[p][q] == 'S':
                    cnt += 1
            if cnt > 3:
                return True
        return False


def so7(n, start):
    global seats
    if n == 0:
        if check(seats):
            global c
            c += 1
        return
    for s in range(start, 26 - n):
        seats.add(s)
        so7(n - 1, s + 1)
        seats.discard(s)


so7(7, 0)
print(c)
