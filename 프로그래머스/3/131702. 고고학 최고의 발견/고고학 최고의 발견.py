def solution(clockHands):
    answer = 0
    n = len(clockHands)
    rotate = [[0]*n for _ in range(n)]
    least = 192
    for rotate_number in range(4**n):
        rotated_cnt = 0
        solved = True
        rotated = [[0]*n]
        for i in range(n-1):
            rotated.append([])
            next_rotate_number = 0
            for j in range(n):
                r = rotate_number % 4
                rotated_cnt += r
                rotate_number //= 4
                rotated[i+1].append(r)
            rotated[i+1].append(0)
            for j in range(n):
                next_rotate_number += (-clockHands[i][j] - sum(rotated[i+1][j-k] for k in range(-1, 2)) - rotated[i][j])%4 * 4**j
            rotate_number = next_rotate_number
        rotated.append([])
        for j in range(n):
            r = rotate_number % 4
            rotated_cnt += r
            rotate_number //= 4
            rotated[n].append(r)
        rotated[n].append(0)
        for j in range(n):
            if (clockHands[n-1][j] + sum(rotated[n][j-k] for k in range(-1, 2)) + rotated[n-1][j]) % 4:
                solved = False
                break
        if solved and rotated_cnt < least:
            least = rotated_cnt
    answer = least
    return answer