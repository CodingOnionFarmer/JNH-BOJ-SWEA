t = int(input())
for tc in range(1, t + 1):
    n, m, c = map(int, input().split())
    hive = [list(map(int, input().split())) for _ in range(n)]
    profits = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n - m + 1):
            chosen = hive[i][j:j + m]
            possible = []
            for num in range(1 << m):
                honey = 0
                profit = 0
                for k in range(m):
                    if num & (1 << k):
                        honey += chosen[k]
                        profit += chosen[k] ** 2
                if honey <= c:
                    possible.append(profit)
            profits[i].append(max(possible))
    twoline_profits = []
    for i in range(n):
        for j in range(i + 1, n):
            twoline_profits.append(max(profits[i]) + max(profits[j]))
    oneline_profits = [0]
    for i in range(n):
        for j in range(n - m + 1):
            for k in range(j + m, n - m + 1):
                oneline_profits.append(profits[i][j] + profits[i][k])
    print(f'#{tc}', max(max(twoline_profits), max(oneline_profits)))
