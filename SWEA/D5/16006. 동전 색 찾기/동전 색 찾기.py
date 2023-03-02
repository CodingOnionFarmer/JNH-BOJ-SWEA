for tc in range(1, int(input()) + 1):
    n = int(input())
    ratio = [0] * 59
    value = list(map(int, input().split()))
    for i in range(n - 1):
        r = value[i + 1] // value[i]
        # if value[i] * r != value[i + 1]:
        #     if value[i] * (r + 1) == value[i + 1]:
        #         r += 1
        #     elif value[i] * (r - 1) == value[i + 1]:
        #         r -= 1
        if r > 60:
            r = 60
        ratio[r - 2] += 1
    ratio_accumulated = [sum(ratio[0:i + 1]) for i in range(59)]
    for i in range(0, 7):
        key = True
        for j in range(59):
            if (j + 2) ** i - 1 < ratio_accumulated[j]:
                key = False
                break
        if key:
            ans = i
            break
    if not ans:
        ans = 1
    print(f'#{tc}', ans)
