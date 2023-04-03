import sys

n, s = map(int, input().split())
seq = list(map(int, sys.stdin.readline().split()))
x = y = 0
length = 100001
now = 0
while y < n:
    if now < s:
        now += seq[y]
        y += 1
    else:
        if y - x < length:
            length = y - x
        now -= seq[x]
        x += 1
while now >= s:
    if y - x < length:
        length = y - x
    now -= seq[x]
    x += 1
if length == 100001:
    length = 0
print(length)
