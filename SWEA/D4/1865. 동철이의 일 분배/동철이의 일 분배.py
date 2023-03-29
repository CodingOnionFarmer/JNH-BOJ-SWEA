def possible_left(d):
    p = 1
    for i in range(d, n):
        p *= max(task[i][j] for j in can_go)
    return p


def dfs(d):
    global percent, max_percent
    if percent * possible_left(d) < max_percent:
        return
    if d == n:
        if percent > max_percent:
            max_percent = percent
        return
    check = {i for i in can_go}
    for i in check:
        if task[d][i]:
            percent *= task[d][i]
            can_go.remove(i)
            dfs(d + 1)
            percent //= task[d][i]
            can_go.add(i)
    return


for tc in range(1, int(input()) + 1):
    n = int(input())
    task = [list(map(int, input().split())) for _ in range(n)]
    max_percent = 0
    percent = 1
    can_go = {i for i in range(n)}
    dfs(0)
    print(f'#{tc}', format(round(max_percent / 100 ** (n - 1), 6), '.6f'))
