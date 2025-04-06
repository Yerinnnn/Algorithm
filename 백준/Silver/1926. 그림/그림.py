import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
picture = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
count = 0
max_size = 0

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    size = 1

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and picture[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                size += 1

    return size

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and not visited[i][j]:
            count += 1
            current_size = bfs(i, j)
            max_size = max(max_size, current_size)

print(count)
print(max_size)