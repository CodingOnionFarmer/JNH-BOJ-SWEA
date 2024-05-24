import heapq

def solution(jobs):
    jobs.sort()
    n = len(jobs)
    now = 0
    will_end_at = 0
    answer = 0
    heap = []
    for i in range(n):
        requested, time = jobs[i]
        while will_end_at <= requested and heap:
            shortest_request = heapq.heappop(heap)
            answer += (len(heap) + 1) * shortest_request
            will_end_at += shortest_request
        if will_end_at <= requested:
            will_end_at = requested + time
            answer += time
        else:
            heapq.heappush(heap, time)
            answer += will_end_at - requested
    while heap:
        answer += len(heap) * heapq.heappop(heap)
    answer //= n
    return answer