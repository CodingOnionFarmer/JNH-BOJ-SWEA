n, k = map(int, input().split())
goto = {n}
visited_even = set()
visited_odd = set()
count = 0
while True:
    k += count
    if k > 500000:
        count = -1
        break
    if k in goto:
        break
    new_goto = set()
    if count % 2:
        if k in visited_odd:
            break
        for i in goto:
            visited_odd.add(i)
        for i in goto:
            for j in [i - 1, i + 1, 2 * i]:
                if 0 < j < 500001 and j not in visited_even:
                    new_goto.add(j)
    else:
        if k in visited_even:
            break
        for i in goto:
            visited_even.add(i)
        for i in goto:
            for j in [i - 1, i + 1, 2 * i]:
                if 0 < j < 500001 and j not in visited_odd:
                    new_goto.add(j)
    goto = new_goto
    count += 1
print(count)
