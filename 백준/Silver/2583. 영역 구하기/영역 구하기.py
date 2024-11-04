from collections import deque

# 상, 하, 좌, 우 네 방향으로 탐색하기 위한 리스트
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 함수 정의
# (x, y)에서 시작하여 연결된 영역의 크기를 구함
def bfs(x, y):
    queue = deque([(x, y)])  # 탐색 시작점을 큐에 삽입
    count = 0  # 현재 영역의 크기 카운트

    while queue:
        cx, cy = queue.popleft()  # 큐에서 현재 위치를 꺼냄
        for dx, dy in directions:  # 네 방향으로 탐색
            nx, ny = cx + dx, cy + dy  # 다음 위치 계산
            # 다음 위치가 격자 안에 있고, 아직 방문하지 않았으며, 직사각형이 아닌 경우
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and not grid[nx][ny]:
                visited[nx][ny] = True  # 방문 표시
                queue.append((nx, ny))  # 큐에 추가
                count += 1  # 영역의 크기 증가
    return count  # 탐색한 영역의 크기 반환

# 행의 수 M, 열의 수 N, 직사각형의 수 K
M, N, K = map(int, input().split())

# 격자판 초기화 (0은 빈 공간, 1은 직사각형 부분)
grid = [[0] * N for _ in range(M)]
# 방문 여부를 기록하는 배열
visited = [[False] * N for _ in range(M)]

# 직사각형 표시
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())  # 직사각형의 왼쪽 아래 (x1, y1)와 오른쪽 위 (x2, y2) 좌표
    # 주어진 좌표 범위 내에서 직사각형 부분을 1로 채움
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1  # 직사각형 부분을 1로 표시

# 각 영역의 개수와 크기 계산
areas = []  # 각 영역의 크기를 저장할 리스트
for i in range(M):  # 행 탐색
    for j in range(N):  # 열 탐색
        # 아직 방문하지 않았고, 직사각형 부분이 아닌 경우 새로운 영역 탐색 시작
        if not visited[i][j] and not grid[i][j]:
            visited[i][j] = True  # 현재 위치 방문 표시
            area_size = bfs(i, j) + 1  # bfs 함수 호출, 자기 자신 포함해서 +1
            areas.append(area_size)  # 탐색된 영역 크기를 리스트에 추가

areas.sort()  # 영역의 넓이를 오름차순으로 정렬 오름차순으로 정렬
print(len(areas))  # 총 영역의 개수 출력
print(*areas)  # 각 영역의 넓이 출력