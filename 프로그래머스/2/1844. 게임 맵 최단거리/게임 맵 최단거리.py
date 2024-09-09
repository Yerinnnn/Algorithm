from collections import deque

def solution(maps):
    n = len(maps)  # 행의 수
    m = len(maps[0])  # 열의 수
    
    # 상, 하, 좌, 우 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # BFS 함수 정의
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        # 방문 배열 초기화
        # 각 위치까지의 최단 거리 기록
        visited = [[0] * m for _ in range(n)]
        visited[x][y] = 1
        
        while queue:
            x, y = queue.popleft()
            
            # 목적지에 도착한 경우
            if x == n - 1 and y == m - 1:
                return visited[x][y]
            
            # 네 방향 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 맵 범위 내이고, 벽이 아니며, 아직 방문하지 않은 경우
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
        
        # 목적지에 도달하지 못한 경우
        return -1
    
    result = bfs(0, 0)
    return result