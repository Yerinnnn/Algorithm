def solution(n, results):
    # 플로이드-워셜 알고리즘을 위한 초기화
    INF = float('inf')
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # 자기 자신으로의 거리는 0
    for i in range(1, n + 1):
        graph[i][i] = 0

    # 결과에 따른 그래프 초기화 (단방향)
    for winner, loser in results:
        graph[winner][loser] = 1  # winner가 loser를 이김

    # 플로이드-워셜 알고리즘을 사용하여 모든 쌍의 최단 경로를 계산
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    # 순위를 알 수 있는 학생 수 계산
    count = 0
    for i in range(1, n + 1):
        known_count = 0
        # 선수 i가 자기 자신을 제외한 모든 다른 선수와의 관계를 아는지 확인
        for j in range(1, n + 1):
            if i != j and (graph[i][j] < INF or graph[j][i] < INF):
                known_count += 1
        # i번 선수가 모든 다른 선수와의 승패 관계를 알고 있는 경우
        if known_count == n - 1:
            count += 1
    
    return count