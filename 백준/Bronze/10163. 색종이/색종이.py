n = int(input())
paper = [[0] * 1001 for _ in range(1001)]
for i in range(n):
    x, y, dx, dy = map(int, input().split())
    for j in range(x, x + dx):
        for k in range(y, y + dy):
            paper[j][k] = i + 1
cnt = [0] * 1001
for j in range(1001):
    for k in range(1001):
        num = paper[j][k]
        cnt[num] += 1
for i in range(n):
    print(cnt[i+1])
