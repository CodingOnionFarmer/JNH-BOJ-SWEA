def bd(num):  # binary digits
    if not num:
        return 0, 0
    x = 1
    while not num % 2:
        x += 1
        num //= 2
    y = x - 1
    while num:
        y += 1
        num //= 2
    return x, y


def dfs(now, depth, digit):
    # print(now, depth, digit, '탐험')
    global found
    if depth == n:
        found = True
        return
    if found:
        return
    if digit > 59 - (n - depth):
        return
    move = set()
    smallest = 60
    for i in range(n):
        if not visited[i]:
            x, y = distance[now][i]
            # print(i, x, y, 'ixy')
            if x <= digit:
                return
            if x <= smallest:
                if x < smallest:
                    smallest = x
                    move.clear()
                move.add((i, y))
    for i, y in move:
        visited[i] = True
        dfs(i, depth + 1, y)
        visited[i] = False
    return


for tc in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))
    distance = [[bd(abs(numbers[i] - numbers[j])) for i in range(n)] for j in range(n)]
    visited = [False] * n
    found = False
    for i in range(n):
        visited[i] = True
        dfs(i, 1, 0)
        if found:
            break
        visited[i] = False
    ans = 'no'
    if found:
        ans = 'yes'
    print(f'#{tc + 1}', ans)
