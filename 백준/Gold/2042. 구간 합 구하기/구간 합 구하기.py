import sys

input = sys.stdin.readline
print = sys.stdout.write
n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
stree = [0] * (4 * n)


def merge(left, right):
    return left + right


def build(node, left, right):
    if left == right:
        stree[node] = nums[left]
        return stree[node]
    mid = (left + right) // 2
    left_val = build(2 * node, left, mid)
    right_val = build(2 * node + 1, mid + 1, right)
    stree[node] = merge(left_val, right_val)
    return stree[node]


def query(start, end, node, left, right):
    if end < left or start > right:
        return 0
    if start <= left and end >= right:
        return stree[node]
    mid = (left + right) // 2
    left_val = query(start, end, 2 * node, left, mid)
    right_val = query(start, end, 2 * node + 1, mid + 1, right)
    return merge(left_val, right_val)


def update(idx, val, node, left, right):
    if idx < left or idx > right:
        return stree[node]
    if left == right:
        stree[node] = val
        return stree[node]
    mid = (left + right) // 2
    left_val = update(idx, val, 2 * node, left, mid)
    right_val = update(idx, val, 2 * node + 1, mid + 1, right)
    stree[node] = merge(left_val, right_val)
    return stree[node]


build(1, 0, len(nums) - 1)
for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b - 1, c, 1, 0, len(nums) - 1)
    else:
        print(str(query(b - 1, c - 1, 1, 0, len(nums) - 1)))
        print('\n')
