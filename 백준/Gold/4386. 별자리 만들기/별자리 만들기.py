n = int(input())
stars = [tuple(map(float, input().split())) for _ in range(n)]
arr = []
for i in range(n - 1):
    for j in range(i + 1, n):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        arr.append((distance, i, j))
arr.sort()
parent = [i for i in range(n)]
result = 0


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    p, q = find(x), find(y)
    parent[max(p, q)] = parent[min(p, q)]


for cost, a, b in arr:
    if find(a) != find(b):
        union(a, b)
        result += cost
print(round(result, 2))
