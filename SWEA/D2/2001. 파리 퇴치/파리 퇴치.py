t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    flies = []
    for _ in range(n):
        flies.append(list(map(int, input().split())))
    max_kill = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            kill = 0
            for k in range(m):
                for l in range(m):
                    kill += flies[i + k][j + l]
            if kill > max_kill:
                max_kill = kill
    print(f'#{tc}', max_kill)
