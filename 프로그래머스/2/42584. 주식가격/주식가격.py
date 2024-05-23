import heapq

def solution(prices):
    n = len(prices)
    answer = [0] * n
    heap = []
    for i in range(n):
        price = prices[i]
        while heap:
            mp, idx = heapq.heappop(heap)
            if price >= -mp:
                heapq.heappush(heap, (mp, idx))
                break
            answer[idx] = i - idx
        heapq.heappush(heap, (-price, i))
    while heap:
        mp, idx = heapq.heappop(heap)
        answer[idx] = n - idx - 1
    return answer