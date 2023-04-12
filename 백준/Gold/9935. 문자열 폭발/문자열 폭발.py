word, bomb = input(), input()
result = []
p = 0
ps = []
for i in range(len(word)):
    if word[i] == bomb[p]:
        if p == len(bomb) - 1:
            for j in range(len(bomb) - 1):
                result.pop()
            if ps:
                p = ps[-1]
                ps.pop()
            else:
                p = 0
        else:
            p += 1
            result.append(word[i])
    elif word[i] == bomb[0]:
        ps.append(p)
        result.append(word[i])
        p = 1
    else:
        result.append(word[i])
        p = 0
        ps.clear()
if result:
    print(''.join(result))
else:
    print('FRULA')
