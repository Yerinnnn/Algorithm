import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빙산이 녹은 후 상태를 반환하는 함수
def melt_iceberg():
    global iceberg
    melted = [[0] * M for _ in range(N)]  # 각 빙산의 감소량 저장
    
    # 각 빙산이 녹을 양 계산
    for x in range(N):
        for y in range(M):
            if iceberg[x][y] > 0:  # 빙산이 존재하는 경우
                water_count = 0  # 인접한 바닷물 개수
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M and iceberg[nx][ny] == 0:
                        water_count += 1
                melted[x][y] = water_count

    # 녹이기 (빙산 높이 감소)
    for x in range(N):
        for y in range(M):
            iceberg[x][y] = max(0, iceberg[x][y] - melted[x][y])

# BFS로 빙산 덩어리 개수 세기
def count_iceberg():
    visited = [[False] * M for _ in range(N)]
    count = 0  # 덩어리 개수
    
    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        
        while queue:
            cx, cy = queue.popleft()
            for d in range(4):
                nx, ny = cx + dx[d], cy + dy[d]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and iceberg[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    for x in range(N):
        for y in range(M):
            if iceberg[x][y] > 0 and not visited[x][y]:  # 빙산 발견
                count += 1
                if count > 1:  # 두 개 이상이면 바로 반환
                    return count
                bfs(x, y)  # BFS 실행

    return count

N, M = map(int, sys.stdin.readline().split())
iceberg = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

time = 0

while True:
    melt_iceberg()  # 1년 경과 -> 빙산 녹이기
    time += 1  # 시간 증가

    num_of_icebergs = count_iceberg()  # 빙산 덩어리 개수 확인
    
    if num_of_icebergs >= 2:  # 빙산이 두 덩어리 이상이면 종료
        print(time)
        break
    if num_of_icebergs == 0:  # 빙산이 모두 녹은 경우
        print(0)
        break