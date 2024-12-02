import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def find_depth_and_parent(root, tree, depth, parent):
    """DFS로 각 노드의 깊이와 부모를 계산하기"""
    stack = [(root, 0, -1)]  # (현재 노드, 깊이, 부모 노드)
    while stack:
        node, d, p = stack.pop()
        depth[node] = d
        parent[node] = p
        for child in tree[node]:
            if child != p:  # 부모로 다시 돌아가지 않도록
                stack.append((child, d + 1, node))

def find_lca(a, b, depth, parent):
    """두 노드 a, b의 가장 가까운 공통 조상(LCA)을 찾기"""
    # 두 노드의 깊이를 맞춤
    while depth[a] > depth[b]:
        a = parent[a]
    while depth[b] > depth[a]:
        b = parent[b]

    # 공통 조상을 찾을 때까지 부모로 거슬러 올라감
    while a != b:
        a = parent[a]
        b = parent[b]

    return a

t = int(input())

for _ in range(t):
    n = int(input())  # 노드 개수
    tree = defaultdict(list)
    parent_count = [0] * (n + 1)  # 부모 노드 개수로 루트를 판단

    for _ in range(n - 1):
        a, b = map(int, input().split())  # a가 b의 부모
        tree[a].append(b)
        tree[b].append(a)
        parent_count[b] += 1

    root = parent_count.index(0, 1)

    # 깊이와 부모 정보 계산
    depth = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    find_depth_and_parent(root, tree, depth, parent)

    # 두 노드 입력
    a, b = map(int, input().split())

    print(find_lca(a, b, depth, parent))