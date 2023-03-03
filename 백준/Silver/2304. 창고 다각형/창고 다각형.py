n = int(input())
height = [0] * 1001
for _ in range(n):
    l, h = map(int, input().split())
    height[l] = h
highest = max(height)
from_left = 0
from_right = 1000
now = 0
area = 0
while height[from_left] < highest:
    now = max(now, height[from_left])
    area += now
    from_left += 1
now = 0
while height[from_right] < highest:
    now = max(now, height[from_right])
    area += now
    from_right -= 1
print(area + (from_right - from_left + 1) * highest)
