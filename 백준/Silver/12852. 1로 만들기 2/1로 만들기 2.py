made = {1: [1]}
cnt = 0
visited = set()
n = int(input())
while n not in made:
    make = {}
    for i in made:
        visited.add(i)
    for i in made:
        if i + 1 not in make and i + 1 not in visited:
            make[i + 1] = made[i] + [i + 1]
        if 2 * i <= n and 2 * i not in make and 2 * i not in visited:
            make[2 * i] = made[i] + [2 * i]
        if 3 * i <= n and 3 * i not in make and 3 * i not in visited:
            make[3 * i] = made[i] + [3 * i]
    made = make
    cnt += 1
print(cnt)
print(*sorted(made[n], reverse=True))
