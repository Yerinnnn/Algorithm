import sys
from collections import defaultdict
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 노드의 개수, 각 노드의 가중치, 트리 구조 저장
n = int(input())
weights = [0] + list(map(int, input().split()))
tree = defaultdict(list)

# 트리 간선 입력
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(n + 1)]  # dp[u][0], dp[u][1]
visited = [False] * (n + 1)  # 노드 방문 여부
selected = [[] for _ in range(n + 1)]  # 최적 구성원을 추적

def dfs(node):
    visited[node] = True
    dp[node][1] = weights[node]  # 현재 노드를 포함하는 경우의 초기값은 자신의 가중치
    
    for neighbor in tree[node]:
        if not visited[neighbor]:  # 아직 방문하지 않은 자식 노드만 처리
            dfs(neighbor)
            
            # 현재 노드를 포함하지 않는 경우 (자식 노드를 포함할 수도 있음)
            dp[node][0] += max(dp[neighbor][0], dp[neighbor][1])
            
            # 현재 노드를 포함하는 경우 (자식 노드를 반드시 포함하지 않아야 함)
            dp[node][1] += dp[neighbor][0]

# 독립 집합 구성 추적 함수
def find_members(node, include):
    visited[node] = True
    if include:  # 현재 노드를 포함하는 경우
        members.append(node)
        for neighbor in tree[node]:
            if not visited[neighbor]:
                find_members(neighbor, False)
    else:  # 현재 노드를 포함하지 않는 경우
        for neighbor in tree[node]:
            if not visited[neighbor]:
                if dp[neighbor][0] >= dp[neighbor][1]:
                    find_members(neighbor, False)
                else:
                    find_members(neighbor, True)

dfs(1)

members = []
visited = [False] * (n + 1)
if dp[1][0] >= dp[1][1]:
    find_members(1, False)
else:
    find_members(1, True)

members.sort()
print(max(dp[1][0], dp[1][1]))  # 최대 가중치 출력
print(" ".join(map(str, members)))  # 최적 구성원 출력