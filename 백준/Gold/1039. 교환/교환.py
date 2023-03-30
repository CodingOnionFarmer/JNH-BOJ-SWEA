n, m = input().split()
m = int(m)
ln = list(n)
make = {''.join(ln)}
for i in range(m):
    new_make = set()
    for s in make:
        for j in range(len(ln) - 1):
            for k in range(j + 1, len(ln)):
                ls = list(s)
                ls[j], ls[k] = ls[k], ls[j]
                if ls[0] == '0':
                    continue
                new_make.add(''.join(ls))
    make = new_make
if make:
    print(max(make))
else:
    print(-1)
