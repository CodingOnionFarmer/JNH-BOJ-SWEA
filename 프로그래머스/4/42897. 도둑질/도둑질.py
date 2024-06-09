def solution(money):
    a, b, c, d = money[0], -1001, -1001, 0
    for i in range(1, len(money) - 1):
        a, b, c, d = b + money[i], max(a, b), d + money[i], max(c, d)
    answer = max(a, b, c, d + money[-1])
    return answer