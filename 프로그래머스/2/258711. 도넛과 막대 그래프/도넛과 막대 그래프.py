from collections import defaultdict

def solution(edges):
    # 1. 그래프의 간선 개수 저장
    edge_counts = defaultdict(lambda: [0, 0])  # {노드: [out-degree, in-degree]}

    for a, b in edges:
        edge_counts[a][0] += 1  # a에서 나가는 간선
        edge_counts[b][1] += 1  # b로 들어오는 간선

    # 2. 생성 노드 찾기 (나가는 간선이 2개 이상 & 들어오는 간선이 없음)
    answer = [0, 0, 0, 0]

    for node, (out_degree, in_degree) in edge_counts.items():
        if out_degree >= 2 and in_degree == 0:
            answer[0] = node  # 생성 노드

    # 3. 그래프 유형 카운트
    for node, (out_degree, in_degree) in edge_counts.items():
        if node == answer[0]:
            continue  # 생성 노드는 그래프 분류에서 제외

        if out_degree == 0 and in_degree > 0:
            answer[2] += 1  # 막대 모양 그래프
        elif out_degree >= 2 and in_degree >= 2:
            answer[3] += 1  # 8자 모양 그래프

    # 4. 도넛 개수 계산
    answer[1] = edge_counts[answer[0]][0] - answer[2] - answer[3]

    return answer
