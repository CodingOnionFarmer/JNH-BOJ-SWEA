c_paper = [5] * 5
paper = [list(map(int, input().split())) for _ in range(10)]
cover = [(i, j) for i in range(10) for j in range(10) if paper[i][j]] + [(10, 10)]
visited = set()
c = len(cover) - 1
p = 0
cnt = 26


def dfs():
    global p
    while cover[p] in visited:
        p += 1
    if p == c:
        global cnt
        if cnt > 25 - sum(c_paper):
            cnt = 25 - sum(c_paper)
        return
    x, y = cover[p]
    fix = p
    for i in range(min(5, 10 - x, 10 - y)):
        if c_paper[i] and all(
                paper[x + j][y + k] and (x + j, y + k) not in visited for j in range(i + 1) for k in range(i + 1)):
            c_paper[i] -= 1
            for j in range(i + 1):
                for k in range(i + 1):
                    visited.add((x + j, y + k))
            dfs()
            c_paper[i] += 1
            p = fix
            for j in range(i + 1):
                for k in range(i + 1):
                    visited.remove((x + j, y + k))
    return


dfs()
if cnt > 25:
    cnt = -1
print(cnt)
