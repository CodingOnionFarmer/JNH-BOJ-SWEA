n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))

best = {}
for i in range(1, n):
    if i == 1 or i == 2:
        best[n - i] = stairs[n]
    elif i == 3:
        best[n - i] = max(stairs[n - 2], stairs[n - 1]) + stairs[n]
    else:
        best[n - i] = max(best[n - i + 2] + stairs[n - i + 2], best[n - i + 3] + stairs[n - i + 1] + stairs[n - i + 3])

if n == 1:
    print(stairs[1])
elif n == 2:
    print(stairs[1] + stairs[2])
else:
    print(max(stairs[1] + best[1], stairs[2] + best[2]))
