n, b = map(int, input().split())
ma = [list(map(int, input().split())) for _ in range(n)]
ma = [[num % 1000 for num in row] for row in ma]
remainder = []
while b > 1:
    if b % 2:
        remainder.append(ma)
    ma = [[sum(ma[i][k] * ma[k][j] for k in range(n)) % 1000 for j in range(n)] for i in range(n)]
    b //= 2
for r in remainder:
    ma = [[sum(ma[i][k] * r[k][j] for k in range(n)) % 1000 for j in range(n)] for i in range(n)]
for row in ma:
    print(*row)
