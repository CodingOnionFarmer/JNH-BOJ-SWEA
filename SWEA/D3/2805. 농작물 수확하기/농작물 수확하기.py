t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    price = 0
    for i in range(n):
        farm_line = input()
        price += sum(map(int, farm_line[abs(n // 2 - i):n - abs(n // 2 - i)]))
    print(f'#{tc}', price)
