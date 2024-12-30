from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 외부 공기 탐색 및 접촉 치즈 찾기
def find_air():
    queue = deque([(0, 0)])  # 격자 밖에서 시작
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    is_contacted = [[0] * M for _ in range(N)]  # 접촉 면 기록

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if grid[nx][ny] == 0:  # 공기
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif grid[nx][ny] == 1:  # 치즈
                    is_contacted[nx][ny] += 1  # 접촉 면 증가

    return is_contacted

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

time = 0

while True:
    is_contacted = find_air()  # 외부 공기와 접촉한 치즈 찾기
    melted = False

    for x in range(N):
        for y in range(M):
            # 2면 이상 접촉한 치즈를 녹임
            if grid[x][y] == 1 and is_contacted[x][y] >= 2:
                grid[x][y] = 0
                melted = True

    if not melted:  # 녹을 치즈가 없으면 종료
        break

    time += 1  # 시간 증가

print(time)