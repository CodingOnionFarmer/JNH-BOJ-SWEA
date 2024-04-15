def solution(e, starts):
    yaksu = [2] * (e+1)
    yaksu[1] = 1
    for n in range(2, e+1):
        if n*n > e:
            break
        for m in range(n, e//n + 1):
            yaksu[n*m] += 2
        yaksu[n*n] -= 1
    most_num = [0] * (e+1)
    p = e
    most = 0
    num = 0
    while p:
        if yaksu[p] >= most:
            num = p
            most = yaksu[p]
        most_num[p] = num
        p -= 1
    answer = [most_num[i] for i in starts]
    return answer