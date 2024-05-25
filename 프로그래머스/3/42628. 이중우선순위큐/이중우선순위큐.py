import heapq

def solution(operations):
    heap_min = []
    heap_max = []
    queue = {}
    heap_length = 0
    answer = []
    for i in range(len(operations)):
        op, num = operations[i].split()
        num = int(num)
        if op == 'I':
            heapq.heappush(heap_min, num)
            heapq.heappush(heap_max, -num)
            if num in queue:
                queue[num] += 1
            else:
                queue[num] = 1
            heap_length += 1
        elif not heap_length:
            pass
        elif num == 1:
            while True:
                deleted = -heapq.heappop(heap_max)
                if queue[deleted]:
                    queue[deleted] -= 1
                    break
            heap_length -= 1
        else:
            while True:
                deleted = heapq.heappop(heap_min)
                if queue[deleted]:
                    queue[deleted] -= 1
                    break
            heap_length -= 1
    if not heap_length:
        return [0,0]
    while True:
        maximum = -heapq.heappop(heap_max)
        if queue[maximum]:
            answer.append(maximum)
            break
    while True:
        minimum = heapq.heappop(heap_min)
        if queue[minimum]:
            answer.append(minimum)
            break
    return answer