for tc in range(1, 11):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for i in range(100):
        N = False
        for j in range(100):
            if table[j][i] == 1:
                N = True
            if table[j][i] == 2 and N:
                cnt += 1
                N = False
    print(f'#{tc}', cnt)
