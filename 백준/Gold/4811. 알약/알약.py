arr = [[] for _ in range(30)]
arr[0].append(1)
arr[1].append(1)
for i in range(2, 30):
    arr[i].append(0)

for i in range(29):
    arr[0].append(arr[0][i] + arr[1][i])
    for j in range(1, 29):
        arr[j].append(arr[j - 1][i] + 2 * arr[j][i] + arr[j + 1][i])
    arr[29].append(0)

while True:
    n = int(input())
    if not n:
        break
    print(arr[0][n - 1])
