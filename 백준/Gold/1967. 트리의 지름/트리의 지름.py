import sys
from collections import defaultdict, deque

input = sys.stdin.readline
sys.setrecursionlimit(100000)  # 재귀 깊이 설정 (트리 깊이가 클 경우 대비)

# 트리 구조
tree = defaultdict(list)

n = int(input().strip())
for _ in range(n - 1):
    # 부모 노드, 자식 노드, 거리
    parent, child, weight = map(int, input().split())
    # 양방향 그래프 구조로 저장 (트리 구조이므로 한 방향만 있어도 됨)
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

def dfs(start):
    # 각 노드의 방문 여부와 거리 기록
    visited = [-1] * (n + 1)
    stack = deque([(start, 0)])  # 스택에 시작 노드와 초기 거리 (0) 추가
    visited[start] = 0           # 시작 노드는 거리 0으로 초기화
    farthest_node, max_distance = start, 0

    # 스택을 이용한 DFS 수행
    while stack:
        current, current_dist = stack.pop()
        
        # 현재 노드와의 거리 정보 갱신 (가장 먼 노드와 거리 기록)
        if current_dist > max_distance:
            farthest_node = current
            max_distance = current_dist
        
        # 인접한 모든 노드를 방문
        for neighbor, dist in tree[current]:
            # 아직 방문하지 않은 노드인 경우
            if visited[neighbor] == -1:
                visited[neighbor] = current_dist + dist
                stack.append((neighbor, current_dist + dist))

    # 가장 먼 노드와 그 노드까지의 거리 반환
    return farthest_node, max_distance

# 순서
# 1. 임의의 노드(1번 노드)에서 가장 먼 노드 찾기
farthest_from_start, _ = dfs(1)

# 2. 첫 번째 DFS로 찾은 노드에서 가장 먼 노드 찾기
_, tree_diameter = dfs(farthest_from_start)

print(tree_diameter)