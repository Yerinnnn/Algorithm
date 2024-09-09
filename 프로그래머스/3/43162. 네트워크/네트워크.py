def solution(n, computers):
    def dfs(v):
        # 현재 노드를 방문 처리
        visited[v] = True
        # 현재 노드와 연결된 모든 노드에 대해
        for i in range(n):
            # 연결되어 있고, 아직 방문하지 않았다면
            if computers[v][i] == 1 and not visited[i]:
                # 재귀적으로 DFS 호출
                dfs(i)
    
    visited = [False] * n
    network_count = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            network_count += 1
            
    return network_count