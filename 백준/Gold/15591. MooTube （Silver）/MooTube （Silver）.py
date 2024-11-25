from collections import deque
import sys
input = sys.stdin.readline

n, q = map(int, input().split())  # n: 동영상 수, q: 쿼리 수
graph = [[] for _ in range(n + 1)]  # 그래프 초기화 (1번부터 n번까지)

# 그래프 입력
for _ in range(n - 1):
    a, b, usado = map(int, input().split())  # a와 b를 연결하는 간선의 유사도 usado
    graph[a].append((b, usado))  # a에서 b로 가는 유사도 저장
    graph[b].append((a, usado))  # b에서 a로 가는 유사도 저장 (무방향 그래프)

for i in range(q):
    k, v = map(int, input().split())  # k: 최소 유사도, v: 시작 동영상
    visited = [False] * (n + 1)  # 방문 체크 배열 (1번부터 n번까지)
    visited[v] = True  # 시작 노드 방문 처리
    result = 0  # 조건을 만족하는 동영상 개수
    q = deque([(v, float('inf'))])  # BFS 큐 초기화 (노드, 현재 유사도)

    while q:
        v, usado = q.pop()  # 현재 노드와 유사도
        for next_v, next_usado in graph[v]:  # 현재 노드에 연결된 모든 인접 노드 탐색
            # 유사도 조건을 만족하고 방문하지 않은 경우
            next_usado = min(usado, next_usado)  # 현재까지의 최소 유사도를 유지
            if next_usado >= k and not visited[next_v]:
                result += 1  # 조건을 만족하는 동영상 개수 증가
                q.append((next_v, next_usado))  # 다음 노드와 유사도 큐에 추가
                visited[next_v] = True  # 방문 처리

    print(result)