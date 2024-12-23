from collections import deque

# 말 이동 방향 (8방향)
horse_moves = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

# 원숭이 이동 방향 (상하좌우)
monkey_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

K = int(input())  # 말처럼 이동할 수 있는 횟수
W, H = map(int, input().split())  # 격자의 너비와 높이
grid = [list(map(int, input().split())) for _ in range(H)]

# 방문 배열: 3차원 (x, y, 남은 말 이동 횟수)
visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]

# BFS 탐색
def bfs():
    queue = deque([(0, 0, K, 0)])  # (x, y, 남은 말 이동 횟수, 이동 횟수)
    visited[0][0][K] = True

    while queue:
        x, y, k, moves = queue.popleft()

        # 목적지에 도달한 경우
        if x == H - 1 and y == W - 1:
            return moves

        # 원숭이 이동 (상하좌우)
        for dx, dy in monkey_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][k] and grid[nx][ny] == 0:
                visited[nx][ny][k] = True
                queue.append((nx, ny, k, moves + 1))

        # 말 이동
        if k > 0:  # 말 이동을 사용할 수 있는 경우
            for dx, dy in horse_moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][k - 1] and grid[nx][ny] == 0:
                    visited[nx][ny][k - 1] = True
                    queue.append((nx, ny, k - 1, moves + 1))

    # 목적지에 도달하지 못한 경우
    return -1

print(bfs())