n, k = map(int, input().split())
if n >= k:
    print(n - k)
    print(1)
else:
    sec = 0
    cnt = 1
    if (n, k) == (0, 1):
        print(1)
        print(1)
    else:
        if n < 2:
            if k >= 2:
                sec = 2 - n
                n = 2
                cnt = 2
        goto = {k: cnt}
        visited = set()

        while n not in goto:
            sec += 1
            for x in goto:
                visited.add(x)
            new_goto = {}
            for x in goto:
                if x % 2:
                    for y in (x - 1, x + 1):
                        if y not in visited:
                            if y not in new_goto:
                                new_goto[y] = goto[x]
                            else:
                                new_goto[y] += goto[x]
                else:
                    if x > n * 4 // 3:
                        y = x // 2
                        if y not in visited:
                            if y not in new_goto:
                                new_goto[y] = goto[x]
                            else:
                                new_goto[y] += goto[x]
                    elif x > n:
                        y = x - 1
                        if y not in visited:
                            if y not in new_goto:
                                new_goto[y] = goto[x]
                            else:
                                new_goto[y] += goto[x]
                    else:
                        y = x + 1
                        if y not in visited:
                            if y not in new_goto:
                                new_goto[y] = goto[x]
                            else:
                                new_goto[y] += goto[x]
            goto = new_goto
        print(sec)
        print(goto[n])
