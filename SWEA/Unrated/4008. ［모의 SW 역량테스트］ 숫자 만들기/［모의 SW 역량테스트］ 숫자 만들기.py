def dfs():
    global d
    global now
    global op
    if d == n:
        global ma
        global mi
        if now > ma:
            ma = now
        if now < mi:
            mi = now
        return
    for i in range(4):
        if op[i]:
            op[i] -= 1
            d += 1
            save = now
            if i == 0:
                now += nums[d - 1]
            elif i == 1:
                now -= nums[d - 1]
            elif i == 2:
                now *= nums[d - 1]
            else:
                save = now
                if now < 0:
                    now *= -1
                    now //= nums[d - 1]
                    now *= -1
                else:
                    now //= nums[d - 1]
            dfs()
            now = save
            op[i] += 1
            d -= 1
    return


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    op = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    now = nums[0]
    d = 1
    ma = -1000000000
    mi = 1000000000
    dfs()
    print(f'#{tc}', ma - mi)
