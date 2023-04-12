def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    p, q = find(x), find(y)
    if (p in know and q in know) or (p not in know and q not in know):
        parent[max(p, q)] = parent[min(p, q)]
    elif p in know:
        parent[q] = parent[p]
    elif q in know:
        parent[p] = parent[q]


n, m = map(int, input().split())
know = list(map(int, input().split()))
know.pop(0)
know = set(know)
parent = [i for i in range(n + 1)]
rep = []
for i in range(m):
    party = list(map(int, input().split()))
    for j in range(1, party[0]):
        union(party[j], party[j + 1])
    rep.append(find(party[1]))
cnt = 0
for p in rep:
    if find(p) not in know:
        cnt += 1
print(cnt)
