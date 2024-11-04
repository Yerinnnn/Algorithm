from collections import deque

# 네 방향 탐색을 위한 리스트
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 함수 정의
# 시작 좌표 (x, y)와 색상 비교 기준을 사용
def bfs(x, y, color, grid, visited):
    queue = deque([(x, y)])  # 탐색 시작점을 큐에 삽입
    visited[x][y] = True  # 시작점 방문 표시

    while queue:
        cx, cy = queue.popleft()  # 현재 위치를 큐에서 꺼냄
        for dx, dy in directions:  # 네 방향 탐색
            nx, ny = cx + dx, cy + dy  # 다음 위치 계산
            # 다음 위치가 그리드 내에 있고, 방문하지 않았으며, 같은 색상인 경우
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True  # 방문 표시
                queue.append((nx, ny))  # 다음 위치를 큐에 추가하여 탐색 지속

# 그리드의 크기 N, 그림
N = int(input())
grid = [list(input().strip()) for _ in range(N)]  # N x N 그리드를 2차원 리스트로 저장

# 일반인의 시각을 위한 방문 배열 초기화 및 영역 개수 초기화
visited_normal = [[False] * N for _ in range(N)]
normal_count = 0  # 일반인의 시각에서의 구역 수

# 적록색약의 시각을 위한 방문 배열 초기화 및 영역 개수 초기화
visited_colorblind = [[False] * N for _ in range(N)]
colorblind_count = 0  # 적록색약의 시각에서의 구역 수

# 일반인 시각의 구역 계산
for i in range(N):
    for j in range(N):
        # 방문하지 않은 위치에서 BFS 탐색 시작
        if not visited_normal[i][j]:
            bfs(i, j, grid[i][j], grid, visited_normal)  # 현재 위치의 색상으로 BFS 탐색
            normal_count += 1  # 새로운 구역이 발견될 때마다 카운트 증가

# 적록색약 시각을 위한 그리드 변환
# 'R'과 'G'를 동일하게 처리
grid_colorblind = [['R' if color == 'G' else color for color in row] for row in grid]

# 적록색약 시각의 구역 계산
for i in range(N):
    for j in range(N):
        # 방문하지 않은 위치에서 BFS 탐색 시작
        if not visited_colorblind[i][j]:
            bfs(i, j, grid_colorblind[i][j], grid_colorblind, visited_colorblind)  # 현재 위치의 색상으로 BFS 탐색
            colorblind_count += 1  # 새로운 구역이 발견될 때마다 카운트 증가

# 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수
print(normal_count, colorblind_count)