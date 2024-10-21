from collections import deque

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
max_height = max(map(max, area))

# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS로 영역을 탐색하는 함수
def bfs(x, y, height, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and area[nx][ny] > height:
                visited[nx][ny] = True
                queue.append((nx, ny))

# 안전 영역을 구하는 함수
def find_safe_areas():
    result = 0
    for h in range(max_height + 1):  # 높이 0부터 최대 높이까지 시도
        visited = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(n):
                if area[i][j] > h and not visited[i][j]:  # 물에 잠기지 않은 영역
                    bfs(i, j, h, visited)
                    count += 1
        result = max(result, count)  # 최대 안전 영역 개수 갱신
    return result

print(find_safe_areas())