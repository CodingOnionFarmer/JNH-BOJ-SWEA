board = {}
for i in range(-4,23):
    for j in range(-4,23):
        board[(i,j)]=0
for i in range(19):
    numbers = list(map(int, input().split()))
    for j in range(19):
        board[(i, j)] = numbers[j]
key = False
winner = 0
for i in range(19):
    for j in range(19):
        if board[(i, j)]:
            if all(board[(i, j)] == board[i + k, j] for k in range(1, 5)):
                if board[(i, j)] != board[(i - 1, j)]:
                    if board[(i, j)] != board[(i + 5, j)]:
                        key = True
                        winner = board[(i, j)]
                        x = i + 1
                        y = j + 1
                        break
            if all(board[(i, j)] == board[i, j + k] for k in range(1, 5)):
                if board[(i, j)] != board[(i, j + 5)]:
                    if board[(i, j)] != board[(i, j - 1)]:
                        key = True
                        winner = board[(i, j)]
                        x = i + 1
                        y = j + 1
                        break
            if all(board[(i, j)] == board[i + k, j + k] for k in range(1, 5)):
                if board[(i, j)] != board[(i + 5, j + 5)]:
                    if board[(i, j)] != board[(i - 1, j - 1)]:
                        key = True
                        winner = board[(i, j)]
                        x = i + 1
                        y = j + 1
                        break
            if all(board[(i, j)] == board[i - k, j + k] for k in range(1, 5)):
                if board[(i, j)] != board[(i - 5, j + 5)]:
                    if board[(i, j)] != board[(i + 1, j - 1)]:
                        key = True
                        winner = board[(i, j)]
                        x = i + 1
                        y = j + 1
                        break
    if key:
        break
print(winner)
if winner:
    print(x, y, end='')
