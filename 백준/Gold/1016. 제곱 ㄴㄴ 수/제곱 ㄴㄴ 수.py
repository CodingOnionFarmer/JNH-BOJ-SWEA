mi, ma = map(int, input().split())
m = int((ma - 1) ** 0.5) + 1
isprime = [False] * 2 + [True] * (m - 1)
prime = []
for n in range(2, m + 1):
    if isprime[n]:
        prime.append(n)
        for i in range(n ** 2, m, n):
            isprime[i] = False

find = {i for i in range(mi, ma + 1)}
for p in prime:
    p *= p
    for i in range((mi - 1) // p + 1, ma // p + 1):
        find.discard(p * i)
print(len(find))
