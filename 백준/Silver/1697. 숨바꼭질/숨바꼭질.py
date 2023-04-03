n, k = map(int, input().split())
if n > k:
    print(n - k)
else:
    goto = {n}
    visited = set()
    count = 0
    while True:
        if k in goto:
            break
        new_goto = set()
        for i in goto:
            visited.add(i)
        for i in goto:
            for j in [i - 1, i + 1, 2 * i]:
                if 0 < j < k + 2 and j not in visited:
                    new_goto.add(j)
        goto = new_goto
        count += 1
    print(count)
