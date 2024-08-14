from collections import deque

def bfs_shortest_path(grid, start):
    n, m = len(grid), len(grid[0])
    distances = [[-1] * m for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우 이동

    queue = deque([start])
    distances[start[0]][start[1]] = 0 # 시작점의 거리를 0으로 초기화

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))
                
    return distances

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 목표 지점 찾기
start = None
for i in range(N):
    for j in range(M):
        if grid[i][j] == 2:
            start = (i, j)
            break
    if start:
        break

distances = bfs_shortest_path(grid, start)

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            print(0, end=' ')
        else:
            print(distances[i][j], end=' ')
    print()