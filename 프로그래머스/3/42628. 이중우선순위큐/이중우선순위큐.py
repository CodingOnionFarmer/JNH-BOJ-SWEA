import heapq

def solution(operations):
    heap_min = []
    heap_max = []
    heap_length = 0
    for i in range(len(operations)):
        op, num = operations[i].split()
        num = int(num)
        if op == 'I':
            heapq.heappush(heap_min, num)
            heapq.heappush(heap_max, -num)
            heap_length += 1
        elif heap_length <= 1:
            heap_min.clear()
            heap_max.clear()
            heap_length = 0
        elif num == 1:
            heapq.heappop(heap_max)
            heap_length -= 1
        else:
            heapq.heappop(heap_min)
            heap_length -= 1
    if not heap_length:
        return [0,0]
    answer = [-heapq.heappop(heap_max), heapq.heappop(heap_min)]
    return answer