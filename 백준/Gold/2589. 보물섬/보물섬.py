from collections import deque

# 네 방향 탐색을 위한 리스트
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 함수 정의
# 시작 좌표 (x, y)에서 가장 먼 거리 계산
def bfs(x, y):
    # 지도 크기만큼의 방문 배열을 -1로 초기화 (방문하지 않았다고 표시)
    visited = [[-1] * M for _ in range(N)]
    queue = deque([(x, y)])
    visited[x][y] = 0  # 시작 지점 방문 표시 및 거리 0으로 설정
    max_distance = 0  # 최대 거리 저장 변수

    while queue:
        cx, cy = queue.popleft()  # 큐에서 현재 위치를 꺼냄
        for dx, dy in directions:  # 네 방향 탐색
            nx, ny = cx + dx, cy + dy  # 다음 위치 계산
            # 다음 위치가 지도 내에 있고, 방문하지 않았으며, 육지('L')인 경우
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and grid[nx][ny] == 'L':
                visited[nx][ny] = visited[cx][cy] + 1  # 거리 업데이트
                queue.append((nx, ny))  # 다음 위치를 큐에 추가
                max_distance = max(max_distance, visited[nx][ny])  # 최대 거리 갱신

    return max_distance  # 시작 지점에서 가장 먼 거리 반환

# 지도 크기 N x M, 지도 정보
N, M = map(int, input().split())  # 지도 크기 N(행), M(열)
grid = [list(input().strip()) for _ in range(N)]  # 지도 정보 입력

# 보물섬의 최대 거리 저장 변수
max_path = 0

# 모든 육지('L') 좌표에 대해 BFS 실행
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'L':  # 현재 좌표가 육지인 경우
            max_path = max(max_path, bfs(i, j))  # 최대 거리 갱신

# 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간 출력
print(max_path)