def solution(numbers):
    cost = [
        [1,7,6,7,5,4,5,3,2,3],
        [7,1,2,4,2,3,5,4,5,6],
        [6,2,1,2,3,2,3,5,4,5],
        [7,4,2,1,5,3,2,6,5,4],
        [5,2,3,5,1,2,4,2,3,5],
        [4,3,2,3,2,1,2,3,2,3],
        [5,5,3,2,4,2,1,5,3,2],
        [3,4,5,6,2,3,5,1,2,4],
        [2,5,4,5,3,2,3,2,1,2],
        [3,6,5,4,5,3,2,4,2,1]
           ]
    clicks = [int(numbers[i]) for i in range(len(numbers))]
    click = 4
    inf = 7000001
    dp = [inf] * 10
    dp[6] = 0
    for c in clicks:
        next_dp = [set() for _ in range(10)]
        for i in range(10):
            next_dp[i].add(dp[i] + cost[click][c])
            next_dp[click].add(dp[i] + cost[i][c])
        for i in range(10):
            if i == c:
                dp[i] = inf
            else:
                dp[i] = min(next_dp[i])
        click = c
    answer = min(dp)
    return answer