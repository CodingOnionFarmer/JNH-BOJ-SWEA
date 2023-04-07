n = int(input())
m = int(input())
if m:
    broken = list(map(int, input().split()))
else:
    broken = []
working = [i for i in range(10) if i not in broken]
if not working:
    print(abs(n - 100))
elif working == [0]:
    print(min(abs(n - 100), n + 1))
else:
    w = str(n)
    l = len(w)
    lowkey = False
    highkey = False
    whole=True
    fillfrom = l
    for i in range(l):
        if [j for j in working if j < int(w[i])]:
            lowspot = i
            lowkey = True
        if [j for j in working if j > int(w[i])]:
            highspot = i
            highkey = True
        if int(w[i]) not in working:
            whole=False
            break
    if whole:
        print(min(abs(n - 100), l))
    else:
        if lowkey:
            low = list(w)
            low[lowspot] = str(max([j for j in working if j < int(w[lowspot])]))
            for i in range(lowspot + 1, l):
                low[i] = str(max(working))
            low = int(''.join(low))
        else:
            if l > 1:
                low = int(str(max(working)) * (l - 1))
                lowkey = True
        if highkey:
            high = list(w)
            high[highspot] = str(min([j for j in working if j > int(w[highspot])]))
            for i in range(highspot + 1, l):
                high[i] = str(min(working))
            high = int(''.join(high))
        else:
            high = int(str(min([i for i in working if i > 0])) + str(min(working)) * l)
        contrast = [abs(n - 100), high - n + len(str(high))]
        if lowkey:
            contrast.append(n - low + len(str(low)))
        print(min(contrast))
