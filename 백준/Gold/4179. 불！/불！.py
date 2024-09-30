from collections import deque

R, C = map(int, input().split())  # R: 행, C: 열
maze = [list(input().strip()) for _ in range(R)]

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

fire_queue = deque()
jihun_queue = deque()

# 불과 지훈이의 이동 시간 저장
fire_time = [[-1] * C for _ in range(R)]
jihun_time = [[-1] * C for _ in range(R)]

# 불과 지훈이의 초기 위치 찾기
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':  # 불의 위치
            fire_queue.append((i, j))
            fire_time[i][j] = 0  # 불은 시작할 때 시간 0
        elif maze[i][j] == 'J':  # 지훈이의 위치
            jihun_queue.append((i, j))
            jihun_time[i][j] = 0  # 지훈이도 시작할 때 시간 0

# 1. 먼저 불이 퍼지는 BFS
while fire_queue:
    x, y = fire_queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C:  # 미로 내부일 경우
            if maze[nx][ny] != '#' and fire_time[nx][ny] == -1:  # 벽이 아니고 아직 방문하지 않은 곳
                fire_time[nx][ny] = fire_time[x][y] + 1
                fire_queue.append((nx, ny))

# 2. 지훈이의 이동 BFS
while jihun_queue:
    x, y = jihun_queue.popleft()

    # 지훈이가 미로를 탈출했는지 확인
    if x == 0 or x == R-1 or y == 0 or y == C-1:
        print(jihun_time[x][y] + 1)
        exit()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C:  # 미로 내부일 경우
            if maze[nx][ny] == '.' and jihun_time[nx][ny] == -1:  # 벽이 아니고 아직 방문하지 않은 곳
                if fire_time[nx][ny] == -1 or jihun_time[x][y] + 1 < fire_time[nx][ny]:  # 불이 안 퍼졌거나, 지훈이가 불보다 빨리 도착하는 경우
                    jihun_time[nx][ny] = jihun_time[x][y] + 1
                    jihun_queue.append((nx, ny))

# 탈출할 수 없는 경우
print("IMPOSSIBLE")