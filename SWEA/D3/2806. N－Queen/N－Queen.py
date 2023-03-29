def diagonal(x, y):
    for q in queens:
        if abs(x - q[0]) == abs(y - q[1]):
            return False
    return True


def dfs(d):
    if d == n:
        global cnt
        cnt += 1
        return
    for i in list(check):
        if diagonal(d, i):
            queens.append((d, i))
            check.remove(i)
            dfs(d + 1)
            check.add(i)
            queens.pop()
    return


for tc in range(1, int(input()) + 1):
    n = int(input())
    check = {i for i in range(n)}
    queens = []
    cnt = 0
    dfs(0)
    print(f'#{tc}', cnt)
