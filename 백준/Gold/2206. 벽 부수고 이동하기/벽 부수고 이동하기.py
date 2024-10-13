from collections import deque

def bfs(n, m, grid):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 하, 상, 우, 좌
    queue = deque([(0, 0, 0, 1)])  # (x, y, 벽 부순 여부, 거리)
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]  # visited[x][y][벽 부수기 여부]
    visited[0][0][0] = True  # 시작점 방문 처리

    while queue:
        x, y, broken, distance = queue.popleft()

        # 도착점에 도달했을 때
        if x == n - 1 and y == m - 1:
            return distance

        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # 이동할 좌표

            if 0 <= nx < n and 0 <= ny < m:  # 범위 체크
                if grid[nx][ny] == 0 and not visited[nx][ny][broken]:  # 빈 공간
                    visited[nx][ny][broken] = True  # 방문 처리
                    queue.append((nx, ny, broken, distance + 1))  # 큐에 추가
                elif grid[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]:  # 벽
                    visited[nx][ny][1] = True  # 벽을 부순 상태로 방문 처리
                    queue.append((nx, ny, 1, distance + 1))  # 큐에 추가

    return -1  # 도착할 수 없는 경우


n, m = map(int, input().split())  # n: 세로 크기, m: 가로 크기
grid = [list(map(int, input().strip())) for _ in range(n)]  # 맵 정보 입력

result = bfs(n, m, grid)

print(result)