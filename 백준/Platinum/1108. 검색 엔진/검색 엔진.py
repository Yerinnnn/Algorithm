from collections import defaultdict, deque

# 그래프 입력 초기화
n = int(input())
site_number = {}
site_number_cnt = 0
adj = defaultdict(list)
connected = [[0] * 2501 for _ in range(2501)]

# SCC 관련 데이터
visited = [0] * 2501
maked = [0] * 2501
node_id = [0] * 2501
node_id_cnt = 0
st = []
scc_id_cnt = 0
scc = defaultdict(list)
node_scc_id = [0] * 2501
scc_adj = defaultdict(list)
scc_connected = [[0] * 2501 for _ in range(2501)]
indegree = [0] * 2501
score = [1] * 2501
q = deque()

# DFS로 SCC를 찾는 함수
def dfs(here):
    global node_id_cnt, scc_id_cnt
    visited[here] = 1
    node_id_cnt += 1
    node_id[here] = node_id_cnt
    st.append(here)
    parent = node_id[here]

    for there in adj[here]:
        if visited[there] == 0:
            parent = min(parent, dfs(there))
        elif maked[there] == 0:
            parent = min(parent, node_id[there])

    if parent == node_id[here]:
        scc_id_cnt += 1
        this_scc = []

        while True:
            st_top = st.pop()
            this_scc.append(st_top)
            node_scc_id[st_top] = scc_id_cnt
            maked[st_top] = 1
            if st_top == here:
                break

        scc[scc_id_cnt] = this_scc

    return parent

# 위상 정렬을 활용한 SCC 처리 함수
def solve(dest):
    for i in range(1, scc_id_cnt + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        here_scc = q.popleft()

        for there_scc in scc_adj[here_scc]:
            for u in scc[here_scc]:
                for v in scc[there_scc]:
                    if connected[u][v] == 1:
                        score[v] += score[u]

            indegree[there_scc] -= 1
            if indegree[there_scc] == 0:
                q.append(there_scc)

    return score[dest]

# 메인 로직
for _ in range(n):
    line = input().split()
    to = line[0]
    from_number = int(line[1])
    from_sites = line[2:]

    if to not in site_number:
        site_number_cnt += 1
        site_number[to] = site_number_cnt

    for from_ in from_sites:
        if from_ not in site_number:
            site_number_cnt += 1
            site_number[from_] = site_number_cnt

        connected[site_number[from_]][site_number[to]] = 1
        adj[site_number[from_]].append(site_number[to])

dest = input()

# SCC 구성
for i in range(1, site_number_cnt + 1):
    if visited[i] == 0:
        dfs(i)

# SCC 그래프 생성
for i in range(1, site_number_cnt + 1):
    here = i
    for there in adj[i]:
        if node_scc_id[here] != node_scc_id[there] and not scc_connected[node_scc_id[here]][node_scc_id[there]]:
            scc_adj[node_scc_id[here]].append(node_scc_id[there])
            indegree[node_scc_id[there]] += 1
            scc_connected[node_scc_id[here]][node_scc_id[there]] = 1

print(solve(site_number[dest]))