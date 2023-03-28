for tc in range(1, int(input()) + 1):
    n, l = map(int, input().split())
    ingredients = [tuple(map(int, input().split())) for _ in range(n)]
    score = [0] * (l + 1)
    check = {0}
    for i in range(n):
        t, c = ingredients[i]
        for s in sorted(list(check), reverse=True):
            if s + c <= l:
                score[s + c] = max(score[s + c], score[s] + t)
                check.add(s + c)
    print(f'#{tc}', max(score))
