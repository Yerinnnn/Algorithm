from collections import deque

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 외부 공기 탐색
def find_air():
    queue = deque([(0, 0)])  # 격자 밖에서 시작
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 외부 공기인 경우
                if grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                # 치즈와 접촉한 경우
                elif grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    melt.append((nx, ny))  # 녹을 치즈로 추가
    return visited

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

time = 0
last_cheese = 0

while True:
    melt = []  # 이번 시간에 녹을 치즈
    find_air()  # 외부 공기 탐색 및 접촉한 치즈 찾기

    if not melt:  # 녹을 치즈가 없으면 종료
        break

    last_cheese = len(melt)  # 현재 남아있는 치즈 조각 수
    for x, y in melt:  # 치즈 녹이기
        grid[x][y] = 0
    time += 1  # 시간 증가

print(time)
print(last_cheese)