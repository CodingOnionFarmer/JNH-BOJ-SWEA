def push():
    for p in range(36):
        for q in range(51):
            if increase[p][q] > 35:
                increase[p][q + 1] += increase[p][q] // 36
                increase[p][q] %= 36


n = int(input())
if n:
    numbers = [[-1] * 52 for _ in range(n)]
    length = [0] * n
    increase = [[0] * 52 for _ in range(36)]
    for i in range(n):
        num = list(input())
        for j in range(len(num)):
            if num[len(num) - j - 1].isdigit():
                numbers[i][j] = int(num[len(num) - j - 1])
            else:
                numbers[i][j] = ord(num[len(num) - j - 1]) - ord('A') + 10
            increase[numbers[i][j]][j] += 35 - numbers[i][j]
    push()
    for i in range(36):
        increase[i].reverse()
    increase.sort(reverse=True)
    for i in range(36):
        increase[i].reverse()
    k = int(input())
    total = [sum(max(numbers[i][j], 0) for i in range(n)) + sum(increase[i][j] for i in range(k)) for j in range(52)]
    for r in range(51):
        if total[r] > 35:
            total[r + 1] += total[r] // 36
            total[r] %= 36
    d = 51
    while not total[d] and d >= 0:
        d -= 1
    if d < 0:
        print(0)
    while d >= 0:
        if total[d] < 10:
            print(total[d], end='')
        else:
            print(chr(total[d] + ord('A') - 10), end='')
        d -= 1
else:
    print(0)
