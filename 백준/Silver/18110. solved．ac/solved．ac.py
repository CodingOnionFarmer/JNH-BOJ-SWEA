import sys

input = sys.stdin.readline
diff = sorted([int(input()) for _ in range(int(input()))])
if not diff:
    print(0)
else:
    cut = round(3 * len(diff) / 20)
    if 3 * len(diff) / 20 - cut == 0.5:
        cut += 1
    average = round(sum(diff[i] for i in range(cut, len(diff) - cut)) / (len(diff) - cut * 2))
    if sum(diff[i] for i in range(cut, len(diff) - cut)) / (len(diff) - cut * 2) - average == 0.5:
        average += 1
    print(average)
