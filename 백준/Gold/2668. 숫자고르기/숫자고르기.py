import sys

input = sys.stdin.readline

def dfs(v):
    # 현재 노드를 방문했다고 표시
    visited[v] = True
    # 현재 노드가 가리키는 다음 노드
    w = data[v]
    
    # 다음 노드를 아직 방문하지 않았다면 방문
    if not visited[w]:
        dfs(w)
    
    # 다음 노드를 방문했지만 아직 처리가 끝나지 않았다면 (사이클 발견)
    if not finished[w]:
        # 사이클의 시작 노드를 현재 w로 설정
        current = w
        # v에 도달할 때까지 사이클의 모든 노드를 결과에 추가
        while current != v:
            result.append(current)
            current = data[current]
        # 사이클의 마지막 노드(v)도 결과에 추가
        result.append(v)
    
    # 현재 노드의 처리가 완료되었다고 표시
    finished[v] = True

n = int(input())
data = [0] + [int(input()) for _ in range(n)]

visited = [False] * (n + 1)
finished = [False] * (n + 1)
result = []

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)

print(len(result))
for num in sorted(result):
    print(num)