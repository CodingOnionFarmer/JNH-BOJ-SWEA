def solution(n, wires):
    connected = [set() for _ in range(n + 1)]
    for v1, v2 in wires:
        connected[v1].add(v2)
        connected[v2].add(v1)
    visited = [False] * (n + 1)
    
    
    def dfs(v):
        visited[v] = True
        size = 1
        smallest_diff = n
        for c in connected[v]:
            if not visited[c]:
                c_size, c_diff = dfs(c)
                smallest_diff = min(smallest_diff, c_diff, abs(n - 2 * c_size))
                size += c_size
        return size, smallest_diff
    
    
    answer = dfs(1)[1]
    
    return answer