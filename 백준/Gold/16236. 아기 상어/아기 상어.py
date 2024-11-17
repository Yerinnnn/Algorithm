from collections import deque

n = int(input())  # 공간의 크기
space = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 방향 이동 정의
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 아기 상어 초기 상태 설정
shark_size = 2  # 초기 크기
shark_x, shark_y = 0, 0  # 아기 상어의 초기 위치
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:  # 아기 상어 위치
            shark_x, shark_y = i, j
            space[i][j] = 0  # 초기 위치는 빈칸으로 변경

# BFS로 물고기를 찾는 함수
def bfs(x, y, size):
    visited = [[False] * n for _ in range(n)]
    queue = deque([(x, y, 0)])  # (x, y, 거리)
    visited[x][y] = True
    candidates = []

    while queue:
        cx, cy, dist = queue.popleft()

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 상어가 지나갈 수 있는 칸 (빈칸 or 자기 크기 이하 물고기)
                if space[nx][ny] <= size:
                    visited[nx][ny] = True
                    # 먹을 수 있는 물고기
                    if 0 < space[nx][ny] < size:
                        candidates.append((dist + 1, nx, ny))
                    # 빈칸 또는 자기 크기와 같은 물고기
                    else:
                        queue.append((nx, ny, dist + 1))

    # 먹을 수 있는 물고기 중 거리, 위쪽, 왼쪽 순으로 정렬
    candidates.sort()
    return candidates[0] if candidates else None

# 시뮬레이션 실행
time = 0
eat_count = 0

while True:
    # BFS로 가장 가까운 물고기 탐색
    target = bfs(shark_x, shark_y, shark_size)
    if target is None:  # 먹을 수 있는 물고기가 없으면 종료
        break

    # 물고기 먹기
    dist, nx, ny = target
    time += dist  # 이동 시간 누적
    shark_x, shark_y = nx, ny  # 아기 상어 위치 업데이트
    space[nx][ny] = 0  # 먹은 물고기 칸은 빈칸으로 변경
    eat_count += 1

    # 아기 상어 크기 증가
    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

print(time)