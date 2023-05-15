n, k, m = map(int, input().split())

pas = {}
for i in range(m):
    pas[(i, 0)] = 1
    pas[(i, i)] = 1
for i in range(2, m):
    for j in range(1, i):
        pas[(i, j)] = (pas[(i - 1, j)] + pas[(i - 1, j - 1)]) % m


def nkm(n, k, m):
    n1 = n // m
    k1 = k // m
    n %= m
    k %= m
    if k > n:
        return 0
    else:
        if n1 < m and k1 < m:
            return pas[(n, k)] * pas[(n1, k1)] % m
        else:
            return pas[(n, k)] * nkm(n1, k1, m) % m

print(nkm(n,k,m))