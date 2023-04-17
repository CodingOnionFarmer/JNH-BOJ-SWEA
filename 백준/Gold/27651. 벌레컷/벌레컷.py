n = int(input())
size = list(map(int, input().split()))
size_sum = [0]
t = 0
for s in size:
    t += s
    size_sum.append(t)
left = []
p1 = 1
p2 = 2
while True:
    while size_sum[n] - size_sum[p2] >= size_sum[p2] - size_sum[p1]:
        p2 += 1
    if size_sum[p1] >= size_sum[n] - size_sum[p2]:
        break
    left.append(p2)
    p1 += 1
right = []
p1 = 1
p2 = n
while True:
    while size_sum[n] - size_sum[p2] <= size_sum[p1]:
        p2 -= 1
    if size_sum[n] - size_sum[p2] >= size_sum[p2] - size_sum[p1]:
        break
    right.append(p2)
    p1 += 1
print(sum(right[i] - left[i] + 1 for i in range(min(len(left), len(right)))))
