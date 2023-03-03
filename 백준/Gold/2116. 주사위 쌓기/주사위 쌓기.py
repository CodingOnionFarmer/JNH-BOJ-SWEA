import sys

n = int(input())
d = (5, 3, 4, 1, 2, 0)
dice = {}
for i in range(n):
    eye = list(map(int, sys.stdin.readline().split()))
    for j in range(6):
        now = eye[j]
        next = eye[d[j]]
        if min(now, next) == 5:
            score = 4
        elif max(now, next) == 6:
            score = 5
        else:
            score = 6
        dice[(i, now)] = (next, score)
high_score = 0
for j in range(1, 7):
    score = 0
    now = j
    for i in range(n):
        next, sc = dice[(i, now)]
        score += sc
        now = next
    if score > high_score:
        high_score = score
print(high_score)
