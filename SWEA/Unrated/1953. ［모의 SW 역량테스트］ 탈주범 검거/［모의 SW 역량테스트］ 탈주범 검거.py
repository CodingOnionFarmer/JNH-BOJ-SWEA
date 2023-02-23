t = int(input())
for tc in range(1, t + 1):
    n, m, r, c, l = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(n)]
    ty = (
        (0, 0, 0, 0), (1, 1, 1, 1), (1, 0, 1, 0), (0, 1, 0, 1), (1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 1), (1, 0, 0, 1))
    de = ((-1, 0), (0, 1), (1, 0), (0, -1))
    graph = {(i, j): [] for i in range(n) for j in range(m)}
    for i in range(n):
        for j in range(m):
            co = ty[underground[i][j]]
            for k in range(1, 3):
                if co[k]:
                    x, y = i + de[k][0], j + de[k][1]
                    if 0 <= x < n and 0 <= y < m and ty[underground[x][y]][(k + 2) % 4]:
                        graph[(i, j)].append((x, y))
                        graph[(x, y)].append((i, j))
    visited = set()
    goto = {(r, c)}
    for h in range(l):
        for x, y in goto:
            visited.add((x, y))
        new_goto = set()
        for x, y in goto:
            for a, b in graph[(x, y)]:
                if (a, b) not in visited:
                    new_goto.add((a, b))
        goto = new_goto
        if not goto:
            break
    print(f'#{tc}', len(visited))
