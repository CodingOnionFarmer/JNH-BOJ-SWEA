jegob = [1]
for i in range(100000):
    jegob.append((jegob[i] * 2) % 1000000007)

n, k = map(int, input().split())
arr = list(map(int, input().split()))
nums = [0] * k
for i in arr:
    nums[i % k] += 1
answer = 1
for j in range(1, (k + 1) // 2):
    answer *= jegob[nums[j]] + jegob[nums[k - j]] - 1
    answer %= 1000000007
if not k % 2:
    answer *= nums[k // 2] + 1
answer *= nums[0] + 1
answer -= n + 1
answer %= 1000000007

print(answer)