from collections import deque

N, M = map(int, input().split())
pool = [list(map(int, input())) for _ in range(N)]
result = 0

def bfs(h):
    water = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    q = deque()
    
    # 가장자리 체크
    for i in [0, N-1]:
        for j in range(M):
            if not visited[i][j] and pool[i][j] <= h:
                q.append((i, j))
                visited[i][j] = True
                
    for i in range(N):
        for j in [0, M-1]:
            if not visited[i][j] and pool[i][j] <= h:
                q.append((i, j))
                visited[i][j] = True
    
    # BFS로 물이 새나가는 곳 체크
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and pool[nx][ny] <= h:
                visited[nx][ny] = True
                q.append((nx, ny))
    
    # 물이 고이는 칸 계산
    count = 0
    for i in range(N):
        for j in range(M):
            if pool[i][j] <= h and not visited[i][j]:
                count += 1
    return count

for height in range(1, 9):
    result += bfs(height)

print(result)