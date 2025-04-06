import sys
from collections import deque

T = int(sys.stdin.readline())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, graph, visited, M, N):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

    return 1

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                result += bfs(j, i, graph, visited, M, N)

    print(result)