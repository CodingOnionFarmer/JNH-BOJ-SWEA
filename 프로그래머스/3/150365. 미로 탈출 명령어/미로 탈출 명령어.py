def solution(n, m, x, y, r, c, k):
    # d l r u 아래 왼 오른 위
    answer = ''
    down = r - x
    left = y - c
    down_wall = n - x
    left_wall = y - 1
    if k < abs(down)+abs(left) or (k-down-left)%2:
        answer = 'impossible'
        return answer
    if down > 0:
        answer += 'd' * down
        k -= down
        down = 0
        x = r
        down_wall = n - x
    go_down = min((k - abs(down) - abs(left))//2, down_wall)
    answer += 'd' * go_down
    k -= go_down
    x += go_down
    down = r - x
    if left > 0:
        answer += 'l' * left
        k -= left
        left = 0
        y = c
        left_wall = y - 1
    go_left = min((k - abs(down) - abs(left))//2, left_wall)
    answer += 'l' * go_left
    k -= go_left
    y -= go_left
    left = y - c
    go_right_and_left = (k - abs(down) - abs(left))//2
    answer += 'rl' * go_right_and_left
    answer += 'r' * -left
    answer += 'u' * -down
    
    return answer