import sys

m = int(input())
a = 0
for i in range(m):
    n, s = map(int, sys.stdin.readline().split())
    p = 1000000005
    while p:
        if p % 2:
            s = (s * n) % 1000000007
        p //= 2
        n = (n * n) % 1000000007
    a = (a + s) % 1000000007
print(a)
