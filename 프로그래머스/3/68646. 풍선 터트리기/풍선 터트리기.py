def solution(a):
    answer = 0
    n = len(a)
    sfas = [False]*n  # smallest from any side
    snfl = 10**9 + 1  # smallest number from left
    for i in range(n):
        if a[i] < snfl:
            sfas[i] = True
            snfl = a[i]
    snfr = 10**9 + 1  # smallest number from right
    for i in range(n-1, -1, -1):
        if a[i] < snfr:
            sfas[i] = True
            snfr = a[i]
    for i in range(n):
        if sfas[i]:
            answer += 1
    return answer