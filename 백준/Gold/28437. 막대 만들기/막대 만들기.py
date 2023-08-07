n = int(input())
arr = [*map(int, input().split())]
n = int(input())
arr2 = [*map(int, input().split())]
arr.sort()
dp = [0] * (100001)
for i in arr:
    dp[i] = 1

for i in range(1,100001):
    if dp[i]:
        for j in range(2, 100001):
            if i * j > 100000:
                break
            dp[i * j] += dp[i]
for i in arr2:
    print(dp[i], end=" ")
