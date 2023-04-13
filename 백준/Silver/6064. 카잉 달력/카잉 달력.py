import sys
import math

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    g = math.gcd(m, n)
    m //= g
    n //= g
    r = min(x, y)
    x -= r
    y -= r
    if max(x, y) % g:
        print(-1)
    else:
        x //= g
        y //= g
        if x == y == 0:
            print(r)
        else:
            if y > 0:
                for i in range(1, n):
                    if (m * i) % n == y:
                        print(m * i * g + r)
                        break
            else:
                for i in range(1, m):
                    if (n * i) % m == x:
                        print(n * i * g + r)
                        break
