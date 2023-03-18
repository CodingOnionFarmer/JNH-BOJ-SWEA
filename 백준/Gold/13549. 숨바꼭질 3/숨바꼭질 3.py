n, k = map(int, input().split())
if n >= k:
    print(n - k)
else:
    sec = 0
    goto = {k}
    visited = set()
    t = k
    while not t % 2:
        t //= 2
        goto.add(t)
        if t > n:
            goto.discard(2 * t)
    while n not in goto:
        sec += 1
        for x in goto:
            visited.add(x)
        new_goto = set()
        for x in goto:
            t = x + 1
            if t not in visited:
                new_goto.add(t)
            while not t % 2 and t:
                t //= 2
                if t not in visited:
                    new_goto.add(t)
                if t > n:
                    new_goto.discard(2 * t)
            t = x - 1
            if t not in visited:
                new_goto.add(t)
            while not t % 2 and t:
                t //= 2
                if t not in visited:
                    new_goto.add(t)
                if t > n:
                    new_goto.discard(2 * t)
        goto = new_goto
    print(sec)
