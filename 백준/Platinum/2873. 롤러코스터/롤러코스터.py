r, c = map(int, input().split())
if r % 2:
    ans = 'R' * (c - 1) + ('D' + 'L' * (c - 1) + 'D' + 'R' * (c - 1)) * (r // 2)
elif c % 2:
    ans = 'D' * (r - 1) + ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * (c // 2)
else:
    site = [list(map(int, input().split())) for _ in range(r)]
    exclude = 0, 0
    small = 1000
    for i in range(r):
        for j in range((i + 1) % 2, c, 2):
            if site[i][j] < small:
                small = site[i][j]
                exclude = i, j
    a, b = exclude
    if a % 2:
        ans = ('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * (a // 2)
        ans += ('D' * (r - a) + 'R' + 'U' * (r - a) + 'R') * (b // 2)
        ans += 'RD'
        ans += 'RURD' * ((c - b) // 2 - 1)
        ans += ('D' + 'L' * (c - b - 1) + 'D' + 'R' * (c - b - 1)) * ((r - a - 1) // 2)
    else:
        ans = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (b // 2)
        ans += ('R' * (c - b) + 'D' + 'L' * (c - b) + 'D') * (a // 2)
        ans += 'DR'
        ans += 'DLDR' * ((r - a) // 2 - 1)
        ans += ('R' + 'U' * (r - a - 1) + 'R' + 'D' * (r - a - 1)) * ((c - b - 1) // 2)
print(ans)
