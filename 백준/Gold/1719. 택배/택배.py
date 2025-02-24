import sys

INF = float('inf')

N, M = map(int, sys.stdin.readline().split())
dist = [[INF] * (N + 1) for _ in range(N + 1)]
next_step = [[None] * (N + 1) for _ in range(N + 1)]  # 최초 방문할 노드 저장

# 초기화 (자기 자신으로 가는 거리는 0)
for i in range(1, N + 1):
    dist[i][i] = 0

# 간선 입력 (양방향)
for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    dist[a][b] = cost
    dist[b][a] = cost
    next_step[a][b] = b  # 처음 가야 하는 곳 저장
    next_step[b][a] = a  # 반대 방향도 동일

# 플로이드-워셜 알고리즘 실행
for k in range(1, N + 1):  # 경유지
    for i in range(1, N + 1):  # 출발지
        for j in range(1, N + 1):  # 도착지
            if dist[i][j] > dist[i][k] + dist[k][j]:  # 더 짧은 경로 발견
                dist[i][j] = dist[i][k] + dist[k][j]
                next_step[i][j] = next_step[i][k]  # 경유지 업데이트

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            print("-", end=" ")  # 자기 자신은 "-"
        else:
            print(next_step[i][j], end=" ")  # 최단 경로의 첫 번째 경유지 출력
    print()