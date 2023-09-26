import sys

sys.setrecursionlimit(250000)
input = sys.stdin.readline
n = int(input())
total = 0
parents = {}
disjoint_sets = {}
fixed = set()


def find(x):
    if x in parents:
        if parents[x] == x:
            return x
        rx = find(parents[x])
        parents[x] = rx
        return rx
    parents[x] = x
    return x


def union(x, y):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        fixed.add(rx)
    parents[ry] = rx
    return


for i in range(n):
    s, t = map(int, input().split())
    total += s
    total += t
    union(s, t)
for x in parents:
    rx = find(x)
    if rx in disjoint_sets:
        if x in disjoint_sets[rx]:
            fixed.add(rx)
        disjoint_sets[rx].add(x)
    else:
        disjoint_sets[rx] = {x}
for root in disjoint_sets:
    fix = False
    for child in disjoint_sets[root]:
        if child in fixed:
            fix = True
        total -= child
    if not fix:
        total += max(disjoint_sets[root])
print(total)
