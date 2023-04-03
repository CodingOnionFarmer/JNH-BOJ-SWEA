import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    p, q = find(x), find(y)
    parent[max(p, q)] = parent[min(p, q)]


v, e = map(int, input().split())
arr = []
parent = [i for i in range(v + 1)]
for i in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    arr.append((cost, a, b))
arr.sort()
result = 0
for cost, a, b in arr:
    if find(a) != find(b):
        union(a, b)
        result += cost
print(result)
