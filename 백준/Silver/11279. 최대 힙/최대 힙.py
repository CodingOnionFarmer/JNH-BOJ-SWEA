import sys

n = int(input())
heap = []


def heapify_from_top(k):
    global heap
    if 2 * k + 1 >= len(heap):
        return
    a = heap[k]
    b = heap[2 * k + 1]
    if 2 * k + 2 == len(heap):
        if a < b:
            heap[k] = b
            heap[2 * k + 1] = a
            heapify_from_top(2 * k + 1)
    if len(heap) > 2 * k + 2:
        c = heap[2 * k + 2]
        if b > c:
            if a < b:
                heap[k] = b
                heap[2 * k + 1] = a
                heapify_from_top(2 * k + 1)
        else:
            if a < c:
                heap[k] = c
                heap[2 * k + 2] = a
                heapify_from_top(2 * k + 2)


def heapify_from_bottom(k):
    global heap
    if k == 0:
        return
    a = heap[k]
    b = heap[(k - 1) // 2]
    if a > b:
        heap[k] = b
        heap[(k - 1) // 2] = a
        heapify_from_bottom((k - 1) // 2)
    return


for _ in range(n):
    x = int(sys.stdin.readline())
    if x:
        heap.append(x)
        heapify_from_bottom(len(heap) - 1)
    else:
        if heap:
            a = heap[0]
            b = heap[-1]
            print(a)
            heap[0] = b
            heap.pop()
            heapify_from_top(0)
        else:
            print(0)
