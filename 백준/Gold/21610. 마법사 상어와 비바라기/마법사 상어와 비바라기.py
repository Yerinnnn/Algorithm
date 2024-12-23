import sys
input = sys.stdin.readline

# 8방향 정의 (1부터 8까지 순서: ← ↖ ↑ ↗ → ↘ ↓ ↙)
DIRECTION = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

# 대각선 방향 정의
DIAGONAL = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
commands = [tuple(map(int, input().split())) for _ in range(M)]

# 초기 구름 위치 설정
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

for d, s in commands:
    # 1. 모든 구름 이동
    new_clouds = []
    visited = [[False] * N for _ in range(N)]
    
    for x, y in clouds:
        nx = (x + DIRECTION[d][0] * s) % N
        ny = (y + DIRECTION[d][1] * s) % N
        nx = (nx + N) % N  # 음수 모듈러 보정
        ny = (ny + N) % N
        new_clouds.append((nx, ny))
        visited[nx][ny] = True

    # 2. 구름이 있는 칸의 물 양 증가
    for x, y in new_clouds:
        grid[x][y] += 1

    # 3. 대각선 물 복사
    for x, y in new_clouds:
        water_count = 0
        for dx, dy in DIAGONAL:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] > 0:
                water_count += 1
        grid[x][y] += water_count

    # 4. 새로운 구름 생성
    clouds = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] >= 2:
                clouds.append((i, j))
                grid[i][j] -= 2

print(sum(sum(row) for row in grid))