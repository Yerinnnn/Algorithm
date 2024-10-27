from collections import deque

n, m = map(int, input().split())
campus = [input().strip() for _ in range(n)]

# 시작 위치 찾기
start = None
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            start = (i, j)
            break
    if start:
        break

# 방향 벡터 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 초기화
queue = deque([start])
visited = [[False] * m for _ in range(n)]
visited[start[0]][start[1]] = True

# 사람 수 카운팅 초기화
people_count = 0

# BFS 탐색 시작
while queue:
    x, y = queue.popleft()

    # 현재 위치가 'P'인 경우, 사람 수 증가
    if campus[x][y] == 'P':
        people_count += 1

    # 인접한 칸을 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 좌표 유효성 검사 및 방문 여부 확인
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and campus[nx][ny] != 'X':
            visited[nx][ny] = True
            queue.append((nx, ny))

print(people_count if people_count > 0 else "TT")