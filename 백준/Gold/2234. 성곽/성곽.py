from collections import deque

N, M = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(M)]

# 비트마스크 방향 정의 (남, 동, 북, 서)
binary = [8, 4, 2, 1]
dx = [1, 0, -1, 0]  # x 방향 (남, 동, 북, 서)
dy = [0, 1, 0, -1]  # y 방향 (남, 동, 북, 서)

# 변수 초기화
visited = [[0] * N for _ in range(M)]
room_sizes = []  # 각 방의 크기 저장
room_info = [[0] * N for _ in range(M)]  # 각 칸에 방 번호 저장


# BFS를 이용해 방 탐색
def bfs(x, y, room_id):
    queue = deque([(x, y)])
    visited[x][y] = 1
    room_size = 1  # 현재 방의 크기

    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            if not (castle[cx][cy] & binary[d]):  # 벽이 없는 방향인 경우
                nx, ny = cx + dx[d], cy + dy[d]
                if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    room_info[nx][ny] = room_id
                    queue.append((nx, ny))
                    room_size += 1

    return room_size


# 1. 방 탐색 및 최대 방 크기 구하기
room_id = 0  # 방 번호
max_room_size = 0

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            room_info[i][j] = room_id
            size = bfs(i, j, room_id)
            room_sizes.append(size)
            max_room_size = max(max_room_size, size)
            room_id += 1

# 2. 벽 하나 제거했을 때 최대 방 크기 구하기
max_combined_size = 0
for i in range(M):
    for j in range(N):
        for d in range(4):  # 네 방향의 벽 확인
            nx, ny = i + dx[d], j + dy[d]
            if 0 <= nx < M and 0 <= ny < N:  # 인접 칸이 격자 안에 있는 경우
                if room_info[i][j] != room_info[nx][ny]:  # 서로 다른 방인 경우
                    combined_size = room_sizes[room_info[i][j]] + room_sizes[room_info[nx][ny]]
                    max_combined_size = max(max_combined_size, combined_size)

print(room_id)  # 방의 개수
print(max_room_size)  # 가장 큰 방의 크기
print(max_combined_size)  # 벽을 하나 제거했을 때 가장 큰 방의 크기