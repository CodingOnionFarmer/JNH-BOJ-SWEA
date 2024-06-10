def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    r = len(rocks)
    n = r - n
    if n == 1:
        return distance
    rocks.append(0)
    ddn = distance // n  # distance divided by n
    
    
    def binary_search(left, dist):  # left : 위치, dist : 거리, 위치는 실제 위치가 아닌 rocks의 index
        right = r - 1
        goal = rocks[left] + dist
        while left < right:
            mid = (left + right) // 2
            if rocks[mid] < goal:
                if left == mid:
                    return right
                left = mid
            else:
                right = mid
        return left
    
    
    d_left = 0
    d_right = ddn
    while d_left < d_right:
        d_mid = (d_left + d_right + 1) // 2
        p = -1
        d_mid_possible = True
        for i in range(n):
            if r + i <= n + p or distance - rocks[p] < d_mid * (n - i):
                d_mid_possible = False
                break
            p = binary_search(p, d_mid)
        if d_mid_possible:
            d_left = d_mid
        else:
            if d_right == d_mid:
                break
            d_right = d_mid
        
    
    return d_left