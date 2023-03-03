board = [list(input().split()) for _ in range(5)]
nums = set()
for i in range(5):
    for j in range(5):
        num = {((i, j),): board[i][j]}
        for _ in range(5):
            new_num = {}
            for lst in num:
                a, b = lst[-1]
                for x, y in [(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)]:
                    if 0 <= x < 5 and 0 <= y < 5:
                        new_num[lst + ((x, y),)] = num[lst] + board[x][y]
            num = new_num
        for k in num.values():
            nums.add(k)
print(len(nums))
