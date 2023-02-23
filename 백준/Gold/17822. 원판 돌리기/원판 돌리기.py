import sys
from collections import deque

n, m, t = map(int, input().split())
board = [[0] * m] + [deque(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]
c = n * m
s = sum(sum(cir) for cir in board)
for _ in range(t):
    x_, d_, k_ = map(int, input().split())
    if c:
        for i in range(x_, n + 1, x_):
            board[i].rotate(k_ * (-1) ** d_)
        visited = set()
        deleted = False
        for i in range(1, n + 1):
            for j in range(m):
                if (i, j) not in visited and board[i][j]:
                    num = board[i][j]
                    goto = {(i, j)}
                    group = set()
                    while goto:
                        for xy in goto:
                            group.add(xy)
                            visited.add(xy)
                        new_goto = set()
                        for x, y in goto:
                            for a, b in [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)]:
                                if b == m:
                                    b = 0
                                elif b < 0:
                                    b = m - 1
                                if 0 < a < n + 1 and 0 <= b < m and board[a][b] == num and (a, b) not in visited:
                                    new_goto.add((a, b))
                                    group.add((a, b))
                        goto = new_goto
                    if len(group) > 1:
                        for x, y in group:
                            board[x][y] = 0
                        s -= len(group) * num
                        c -= len(group)
                        deleted = True
        if not deleted:
            av = s / c
            for i in range(1, n + 1):
                for j in range(m):
                    num = board[i][j]
                    if num:
                        if num > av:
                            board[i][j] -= 1
                            s -= 1
                        elif num < av:
                            board[i][j] += 1
                            s += 1
print(s)
