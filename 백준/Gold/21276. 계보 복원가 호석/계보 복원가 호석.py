import sys
from collections import defaultdict, deque

input = sys.stdin.readline

# 사람 수
n = int(input())

# 사람 이름 (사전순 정렬을 위해 리스트 사용)
names = list(input().split())
names.sort()

# 사람 이름을 인덱스로 관리하기 위해 딕셔너리 생성
name_idx = {name: idx for idx, name in enumerate(names)}

# 그래프: 각 사람을 key로 하고, 그 사람의 직속 자식을 리스트로 저장
graph = defaultdict(list)

# 진입 차수(부모가 몇 명인지) 저장
indegree = [0] * n

# 관계 수
m = int(input())

# 부모-자식 관계
for _ in range(m):
    child, parent = input().split()

    # parent → child 로 그래프 생성 (parent가 child의 부모다)
    graph[parent].append(child)

    # child의 진입 차수 증가 (부모가 하나 추가됨)
    indegree[name_idx[child]] += 1

# 직속 후손만 정리
children = defaultdict(list)

# 루트 조상 (부모가 없는 사람들) 찾기
roots = []

# 진입 차수가 0인 사람은 최상위 조상 (부모가 없음)
for i in range(n):
    if indegree[i] == 0:
        roots.append(names[i])

# 위상 정렬을 위한 큐 생성
queue = deque()

# 루트부터 탐색 시작
for root in roots:
    queue.append(root)

# 위상 정렬 실행
while queue:
    current = queue.popleft()  # 현재 노드

    # 현재 사람의 직속 자식들 탐색
    for child in graph[current]:
        # 직속 자식 후보로 추가
        indegree[name_idx[child]] -= 1  # 부모 하나 감소시킴

        # 직속 부모가 바로 current이므로 연결
        if indegree[name_idx[child]] == 0:
            # current가 child의 직속 부모이므로 children에 추가
            children[current].append(child)
            queue.append(child)

# 루트 조상 수 출력 + 루트 조상 이름 출력
print(len(roots))
print(' '.join(roots))

# 각 사람의 직속 자식 정보 출력
for name in names:
    # 직속 자식들을 사전순으로 정렬
    children[name].sort()

    # 자식 수와 자식 리스트 출력
    print(f"{name} {len(children[name])} {' '.join(children[name])}")