from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]
# print(maze)
visited = [[False] * m for _ in range(n)]
moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
groups = []
group_map = [[-1] * m for _ in range(n)]
count = 0


def dfs(x, y, t):
    if maze[x][y]:
        return
    global count
    count += 1
    group_map[x][y] = t
    visited[x][y] = True
    for dx, dy in moves:
        if 0 <= x + dx < n and 0 <= y + dy < m and not maze[x + dx][y + dy] and not visited[x + dx][y + dy]:
            dfs(x + dx, y + dy, t)
    return


group_num = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            if not maze[i][j]:
                count = 0
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    group_map[x][y] = group_num
                    count += 1
                    for dx, dy in moves:
                        if 0 <= x + dx < n and 0 <= y + dy < m and not maze[x + dx][y + dy] and not visited[x + dx][
                            y + dy]:
                            q.append((x + dx, y + dy))
                            visited[x + dx][y + dy] = True
                groups.append(count)
                group_num += 1
                count = 0
groups.append(0)
# print('groups', groups)
# print(group_map)
for i in range(n):
    for j in range(m):
        if maze[i][j]:
            can_go_groups = set()
            for dx, dy in moves:
                # print(i, j, dx, dy)
                if 0 <= i + dx < n and 0 <= j + dy < m and not maze[i + dx][j + dy]:
                    can_go_groups.add(group_map[i + dx][j + dy])
            # print(can_go_groups)
            maze[i][j] = (1 + sum(groups[i] for i in can_go_groups)) % 10
            # print(maze)
for i in range(n):
    for j in range(m):
        print(maze[i][j], end='')
    print()
