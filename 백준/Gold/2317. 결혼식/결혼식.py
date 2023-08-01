import sys

input = sys.stdin.readline
n, k = map(int, input().split())
tall = int(input())
short = tall
before = tall
first = tall
last = tall
answer = 0
for i in range(k - 1):
    now = int(input())
    answer += abs(now - before)
    if now > tall:
        tall = now
    elif now < short:
        short = now
    before = now
    last = now
if n-k:
    others = [int(input()) for _ in range(n - k)]
    shortest = min(others)
    tallest = max(others)
    if shortest < short:
        answer += min(2 * (short - shortest), first - shortest, last - shortest)
    if tallest > tall:
        answer += min(2 * (tallest - tall), tallest - first, tallest - last)
print(answer)
