t = int(input())
for tc in range(1, t + 1):
    n, m, k = map(int, input().split())
    answer = 'Possible'
    time = sorted(list(map(int, input().split())))
    for i in range(0, n, k):
        if time[i] < m * (i // k + 1):
            answer = 'Impossible'
            break
    print(f'#{tc}', answer)
