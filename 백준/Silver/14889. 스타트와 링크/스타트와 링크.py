n = int(input())
synergy = []
minimal_difference = 600001
for _ in range(n):
    synergy.append(list(map(int, input().split())))
for num in range(1 << (n - 1)):
    food = []
    for i in range(n - 1):
        if num & (1 << i):
            food.append(i)
    if len(food) == n // 2:
        A = 0
        B = 0
        the_other_food = [i for i in range(n) if i not in food]
        for i in food:
            for j in food:
                A += synergy[i][j]
        for i in the_other_food:
            for j in the_other_food:
                B += synergy[i][j]
        if abs(A - B) < minimal_difference:
            minimal_difference = abs(A - B)
print(minimal_difference)
