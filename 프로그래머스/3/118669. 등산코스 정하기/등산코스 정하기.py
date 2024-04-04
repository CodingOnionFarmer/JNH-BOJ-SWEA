import heapq

def solution(n, paths, gates, summits):
    answer = []
    heap = []
    connected = [[] for i in range(n+1)]
    visited = [False] * (n+1)
    is_gate = [False]* (n+1)
    intensity = 0
    for g in gates:
        is_gate[g] = True
    for p in range(len(paths)):
        path = paths[p]
        i,j,w = path[0],path[1],path[2]
        connected[i].append((w,j))
        connected[j].append((w,i))
    for s in summits:
        visited[s] = True
        for w,p in connected[s]:
            heapq.heappush(heap,(w,s,p))
    while heap:
        w,s,p = heapq.heappop(heap)
        if visited[p]:
            continue
        if is_gate[p]:
            answer = [s,w]
            break
        visited[p] = True
        for new_w, new_p in connected[p]:
            heapq.heappush(heap,(max(w,new_w),s,new_p))
        
            
    return answer