arr = [1]

for i in range(20):
    comb = 1
    next = 0
    for j in range(i + 1):
        left_j = arr[j] * arr[i - j] * comb
        if j > 1:
            left_j //= 2
        if i - j > 1:
            left_j //= 2
        next += left_j
        comb *= (i - j)
        comb //= (j + 1)
    arr.append(next)

for tc in range(int(input())):
    print(arr[int(input())])
