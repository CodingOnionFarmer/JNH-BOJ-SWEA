d = ((-1, 0), (0, 1), (1, 0), (0, -1))
rotate = (3, 0, 1, 2)


def f(a, b):
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr = a + dr
        nc = b + dc
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 0:  # 청소 되지 않은 빈 칸이 있는 경우
                return True
    return False


def f1(a, b, di):
    global cnt

    x, y = d[di]
    na = a + x
    nb = b + y

    if 0 <= na < N and 0 <= nb < M:
        if arr[na][nb] == 0:
            return na, nb  # 앞 칸이 청소되지 안은 빈칸

    return a, b  # 앞칸이 벽이거나 청소가 되어있는 경우


def f2(a, b, di):
    x, y = d[di]
    na = a - x
    nb = b - y

    if 0 <= na < N and 0 <= nb < M:
        if arr[na][nb] == -1:
            return na, nb  # 후진 할 수 있는 경우 후진

    return False  # 후진 할 수 없는 경우


N, M = map(int, input().split())  # 배열의 가로 세로
r, c, direction = map(int, input().split())  # 로봇의 출발 좌표와 바라보는 방향
arr = [list(map(int, input().split())) for i in range(N)]
cnt = 0

while True:

    if arr[r][c] == 0:
        arr[r][c] = -1
        cnt += 1

    if f(r, c):  # 청소되지 않은 칸이 있는지 확인
        # 0 1 2 3
        # 위 좌 우 하
        direction = rotate[direction]

        r, c = f1(r, c, direction)

    else:
        if f2(r, c, direction):  # 후진이 되는지 확인
            r, c = f2(r, c, direction)
        else:
            break

print(cnt)
