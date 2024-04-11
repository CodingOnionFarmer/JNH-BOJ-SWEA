def solution(n, costs):
    answer = 0
    rn = [i for i in range(n + 1)]  # representative number
    costs.sort(key=lambda bridge: bridge[2])
    
    
    def union(a, b):
        rn[max(a,b)] = min(a,b)
        return
    
    
    def find(a):
        if rn[a] == a:
            return a
        b = find(rn[a])
        rn[a] = b
        return b
    
    
    bridges = 0
    cost = 0
    now = 0
    while bridges < n - 1:
        a, b, c = costs[now]
        ra, rb = find(a), find(b)
        if ra != rb:
            union(ra, rb)
            bridges += 1
            cost += c
        now += 1
    answer = cost
    
    return answer