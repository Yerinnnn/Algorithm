import heapq

def dijkstra(start, graph, n):
    distance = [float('inf')] * (n + 1)  # 거리 배열 초기화
    distance[start] = 0  # 시작 노드의 거리 0으로 초기화
    pq = [(0, start)]  # 우선순위 큐 초기화

    while pq:
        current_distance, current_node = heapq.heappop(pq)  # 최단 거리 노드 추출

        if current_distance > distance[current_node]:  # 더 긴 거리일 경우 무시
            continue

        for neighbor, weight in graph[current_node]:  # 인접 노드 탐색
            distance_through_node = current_distance + weight
            if distance_through_node < distance[neighbor]:  # 더 짧은 경로 발견
                distance[neighbor] = distance_through_node
                heapq.heappush(pq, (distance_through_node, neighbor))  # 업데이트된 거리 큐에 추가

    return distance  # 최단 거리 배열 반환


n, m, x = map(int, input().split())  # n: 노드 수, m: 간선 수, x: 파티 장소
graph = [[] for _ in range(n + 1)]  # 인접 리스트 초기화

for _ in range(m):
    u, v, w = map(int, input().split())  # 간선 정보 입력
    graph[u].append((v, w))  # 방향 그래프
    # graph[v].append((u, w))  # 만약 무방향 그래프였다면 이 줄을 활성화

# x에서 모든 노드까지의 최단 경로
distance_from_x = dijkstra(x, graph, n)

# 각 노드에서 x까지의 최단 경로
max_time = 0
for i in range(1, n + 1):
    if i == x:  # 파티 장소는 제외
        continue
    distance_to_x = dijkstra(i, graph, n)  # i에서 x까지의 최단 경로
    total_time = distance_from_x[i] + distance_to_x[x]  # 왕복 시간 계산
    max_time = max(max_time, total_time)  # 최대 시간 업데이트

print(max_time)