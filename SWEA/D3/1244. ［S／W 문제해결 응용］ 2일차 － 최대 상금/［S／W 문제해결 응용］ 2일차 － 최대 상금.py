for tc in range(1, int(input()) + 1):
    n, m = input().split()
    m = int(m)
    ln = list(n)
    big = (''.join(sorted(ln, reverse=True)))
    make = {''.join(ln)}
    for i in range(m):
        new_make = set()
        for s in make:
            for j in range(len(ln) - 1):
                for k in range(j + 1, len(ln)):
                    ls = list(s)
                    ls[j], ls[k] = ls[k], ls[j]
                    new_make.add(''.join(ls))
        make = new_make
    print(f'#{tc}', max(make))
