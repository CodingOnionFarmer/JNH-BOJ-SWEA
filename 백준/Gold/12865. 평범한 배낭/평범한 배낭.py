n, k = map(int, input().split())
wv = []
for _ in range(n):
    wv.append(tuple(map(int, input().split())))
bag = [[0] * (k + 1) for _ in range(n)]
check = {0}
for i in range(n):
    new_check = set()
    for now in check:
        bag[i][now] = bag[i - 1][now]
    for now in check:
        if now + wv[i][0] <= k and bag[i - 1][now] + wv[i][1] > bag[i][now+wv[i][0]]:
            bag[i][now + wv[i][0]] = bag[i - 1][now] + wv[i][1]
            new_check.add(now + wv[i][0])
    check |= new_check
print(max(bag[n - 1]))
