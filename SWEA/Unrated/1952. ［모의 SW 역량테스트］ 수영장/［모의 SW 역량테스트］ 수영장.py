for tc in range(1, int(input()) + 1):
    day, month, month3, year = map(int, input().split())
    plan = list(map(int, input().split()))
    for i in range(12):
        if day * plan[i] > month:
            plan[i] = month
        else:
            plan[i] *= day
    m3 = [plan[i] + plan[i + 1] + plan[i + 2] for i in range(10)]
    month3_use = [sum(plan), month3 + sum(plan) - max(m3), month3 * 2, month3 * 3, month3 * 4]
    combi2 = max(m3[i] + m3[j] for i in range(7) for j in range(i + 3, 10))
    combi3 = max(m3[i] + m3[j] + m3[k] for i in range(4) for j in range(i + 3, 7) for k in range(j + 3, 10))
    month3_use[2] += sum(plan) - combi2
    month3_use[3] += sum(plan) - combi3
    print(f'#{tc}', min(month3_use + [year]))
