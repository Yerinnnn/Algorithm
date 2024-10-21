from collections import deque

# 6방향 (상, 하, 좌, 우, 위, 아래)
dz = [0, 0, 0, 0, 1, -1]
dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]

M, N, H = map(int, input().split())  # 가로, 세로, 높이
tomato = []
queue = deque()

# 토마토 상자의 상태 입력
for h in range(H):
    layer = []
    for n in range(N):
        layer.append(list(map(int, input().split())))
        for m in range(M):
            if layer[n][m] == 1:  # 익은 토마토는 큐에 추가
                queue.append((h, n, m))
    tomato.append(layer)

# BFS로 토마토 익히기
def bfs():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):  # 6방향에 대해 탐색
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = tomato[z][y][x] + 1  # 익는 날짜 갱신
                queue.append((nz, ny, nx))

bfs()  # BFS 수행

# 모든 토마토가 익는 데 걸린 시간 계산
max_days = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 0:  # 익지 않은 토마토가 있으면 -1 출력
                print(-1)
                exit(0)
            max_days = max(max_days, tomato[h][n][m])

# 최초에 익은 상태가 1일이므로 1을 빼줌
print(max_days - 1)