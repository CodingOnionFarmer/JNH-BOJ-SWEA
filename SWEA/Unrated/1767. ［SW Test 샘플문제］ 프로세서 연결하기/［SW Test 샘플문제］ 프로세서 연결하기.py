t = int(input())
# 위 오른 밑 왼
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
from pprint import pprint


def dfs():
    global depth
    global cnt
    global connected
    if depth == len(check):
        global most_connected
        global answer
        if connected > most_connected:
            most_connected = connected
            answer = cnt
        elif connected == most_connected:
            if cnt < answer:
                answer = cnt
        return
    x, y = checklist[depth]
    for k in check[(x, y)]:
        p, q = x + dx[k], y + dy[k]
        while not mexinos[p][q]:
            mexinos[p][q] = 3
            cnt += 1
            p += dx[k]
            q += dy[k]
        if mexinos[p][q] == 3:
            k = (k + 2) % 4
            p += dx[k]
            q += dy[k]
            while mexinos[p][q] == 3:
                mexinos[p][q] = 0
                cnt -= 1
                p += dx[k]
                q += dy[k]
        else:
            connected += 1
            depth += 1
            dfs()
            k = (k + 2) % 4
            p += dx[k]
            q += dy[k]
            while mexinos[p][q] == 3:
                mexinos[p][q] = 0
                cnt -= 1
                p += dx[k]
                q += dy[k]
            connected -= 1
            depth -= 1
    return


for tc in range(1, t + 1):
    n = int(input())
    cnt = 0
    depth = 0
    answer = 100
    checked = 0
    connected = 0
    most_connected = 0
    mexinos = [list(map(int, input().split())) + [2] for _ in range(n)] + [[2] * (n + 1)]
    check = {}
    if mexinos[1][1]:
        if mexinos[1][0] and mexinos[0][1]:
            direction = []
            a, b = 1, 2
            while not mexinos[a][b]:
                b += 1
            if mexinos[a][b] == 2:
                direction.append(1)
            a, b = 2, 1
            while not mexinos[a][b]:
                a += 1
            if mexinos[a][b] == 2:
                direction.append(2)
            if direction:
                check[(1, 1)] = direction
        else:
            checked += 1
    if mexinos[1][n - 2]:
        if mexinos[1][n - 1] and mexinos[0][n - 2]:
            direction = []
            a, b = 1, n - 3
            while not mexinos[a][b]:
                b -= 1
            if mexinos[a][b] == 2:
                direction.append(3)
            a, b = 2, n - 2
            while not mexinos[a][b]:
                a += 1
            if mexinos[a][b] == 2:
                direction.append(2)
            if direction:
                check[(1, n - 2)] = direction
        else:
            checked += 1
    if mexinos[n - 2][1]:
        if mexinos[n - 1][1] and mexinos[n - 2][0]:
            direction = []
            a, b = n - 2, 2
            while not mexinos[a][b]:
                b += 1
            if mexinos[a][b] == 2:
                direction.append(1)
            a, b = n - 3, 1
            while not mexinos[a][b]:
                a -= 1
            if mexinos[a][b] == 2:
                direction.append(0)
            if direction:
                check[(1, 1)] = direction
        else:
            checked += 1
    if mexinos[n - 2][n - 2]:
        if mexinos[n - 2][n - 1] and mexinos[n - 1][n - 2]:
            direction = []
            a, b = n - 3, n - 2
            while not mexinos[a][b]:
                b -= 1
            if mexinos[a][b] == 2:
                direction.append(0)
            a, b = n - 2, n - 3
            while not mexinos[a][b]:
                a -= 1
            if mexinos[a][b] == 2:
                direction.append(3)
            if direction:
                check[(1, 1)] = direction
        else:
            checked += 1
    for i in range(2, n - 2):
        if mexinos[1][i]:
            if mexinos[0][i]:
                direction = []
                for d in (1, 2, 3):
                    a, b = 1 + dx[d], i + dy[d]
                    while not mexinos[a][b]:
                        a += dx[d]
                        b += dy[d]
                    if mexinos[a][b] == 2:
                        direction.append(d)
                if direction:
                    check[(1, i)] = direction
            else:
                checked += 1
        if mexinos[n - 2][i]:
            if mexinos[n - 1][i]:
                direction = []
                for d in (0, 1, 3):
                    a, b = n - 2 + dx[d], i + dy[d]
                    while not mexinos[a][b]:
                        a += dx[d]
                        b += dy[d]
                    if mexinos[a][b] == 2:
                        direction.append(d)
                if direction:
                    check[(n - 2, i)] = direction
            else:
                checked += 1
        if mexinos[i][1]:
            if mexinos[i][0]:
                direction = []
                for d in (0, 1, 2):
                    a, b = i + dx[d], 1 + dy[d]
                    while not mexinos[a][b]:
                        a += dx[d]
                        b += dy[d]
                    if mexinos[a][b] == 2:
                        direction.append(d)
                if direction:
                    check[(i, 1)] = direction
            else:
                checked += 1
        if mexinos[i][n - 2]:
            if mexinos[i][n - 1]:
                direction = []
                for d in (0, 2, 3):
                    a, b = i + dx[d], n - 2 + dy[d]
                    while not mexinos[a][b]:
                        a += dx[d]
                        b += dy[d]
                    if mexinos[a][b] == 2:
                        direction.append(d)
                if direction:
                    check[(i, n - 2)] = direction
            else:
                checked += 1
    for i in range(2, n - 2):
        for j in range(2, n - 2):
            if mexinos[i][j]:
                direction = []
                for d in (0, 1, 2, 3):
                    a, b = i + dx[d], j + dy[d]
                    while not mexinos[a][b]:
                        a += dx[d]
                        b += dy[d]
                    if mexinos[a][b] == 2:
                        direction.append(d)
                if direction:
                    check[(i, j)] = direction
    checklist = list(check.keys())
    dfs()
    print(f'#{tc}', answer + checked)
