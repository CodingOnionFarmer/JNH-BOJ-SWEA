import sys

w, n = map(int, input().split())
item = list(map(int, sys.stdin.readline().split()))
item.sort()
while item and item[-1] > w - 6:
    item.pop()
item.reverse()
while item and item[-1] < w - 599993:
    item.pop()
item.sort()
n = len(item)
lo = {i: [] for i in range(w // 2)}
hi = {i: [] for i in range(w // 2 + 1, w)}
for i in range(n - 1):
    for j in range(i + 1, n):
        if item[i] + item[j] in lo and len(lo[item[i] + item[j]]) < 2:
            lo[item[i] + item[j]].append({i, j})
        elif item[i] + item[j] in hi and len(hi[item[i] + item[j]]) < 2:
            hi[item[i] + item[j]].append({i, j})
x = 3
ans = 'NO'
while x < w // 2:
    if lo[x] and hi[w - x]:
        if len(lo[x][0] | hi[w - x][0]) == 4:
            ans = 'YES'
            break
        if len(lo[x]) > 1:
            if len(lo[x][1] | hi[w - x][0]) == 4:
                ans = 'YES'
                break
            if len(lo[x]) > 2:
                ans = 'YES'
                break
            if len(hi[w - x]) > 1:
                ans = 'YES'
                break
        if len(hi[w - x]) > 1:
            if len(lo[x][0] | hi[w - x][1]) == 4:
                ans = 'YES'
                break
            if len(hi[w - x]) > 2:
                ans = 'YES'
                break
    x += 1
print(ans)
