from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

# 상하좌우 이동
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 탐색
def bfs():
    # (x, y, remaining_k, distance)
    queue = deque([(0, 0, K, 1)])
    visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]
    visited[0][0][K] = True

    while queue:
        x, y, remaining_k, distance = queue.popleft()

        # 도착점에 도달한 경우
        if x == N - 1 and y == M - 1:
            return distance

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 범위 체크
            if 0 <= nx < N and 0 <= ny < M:
                # 빈 칸이고 방문하지 않았다면 이동
                if grid[nx][ny] == 0 and not visited[nx][ny][remaining_k]:
                    visited[nx][ny][remaining_k] = True
                    queue.append((nx, ny, remaining_k, distance + 1))
                # 벽이고 벽을 부술 수 있는 경우
                elif grid[nx][ny] == 1 and remaining_k > 0 and not visited[nx][ny][remaining_k - 1]:
                    visited[nx][ny][remaining_k - 1] = True
                    queue.append((nx, ny, remaining_k - 1, distance + 1))

    # 도달할 수 없는 경우
    return -1

print(bfs())