b = (1, 0)
t = ((1, 2), (0, 2), (0, 1))
for tc in range(1, int(input()) + 1):
    bi = list(input())
    tri = list(input())
    answer = 0
    for i in range(1, len(bi)):
        for j in range(len(tri)):
            for k in range(2):
                bi[i] = str(b[int(bi[i])])
                s = tri[j]
                tri[j] = str(t[int(tri[j])][k])
                if int(''.join(bi), 2) == int(''.join(tri), 3):
                    answer = int(''.join(bi), 2)
                    break
                bi[i] = str(b[int(bi[i])])
                tri[j] = s
            if answer:
                break
        if answer:
            break
    print(f'#{tc}', answer)
