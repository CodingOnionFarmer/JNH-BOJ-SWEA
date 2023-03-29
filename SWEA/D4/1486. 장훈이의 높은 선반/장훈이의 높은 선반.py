for tc in range(1, int(input()) + 1):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    m = sum(height) - b
    exclude = {0}
    for i in range(n):
        if height[i] > m:
            pass
        for e in list(exclude):
            if e + height[i] <= m:
                exclude.add(e + height[i])
    print(f'#{tc}', m - max(exclude))
