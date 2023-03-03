for _ in range(4):
    a1, b1, a2, b2, x1, y1, x2, y2 = map(int, input().split())
    x = (x1 - a2) * (x2 - a1)
    y = (y1 - b2) * (y2 - b1)
    if x > 0 or y > 0:
        print('d')
    elif not x + y:
        print('c')
    elif not x * y:
        print('b')
    else:
        print('a')
