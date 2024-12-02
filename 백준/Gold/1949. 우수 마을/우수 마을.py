import sys
from collections import defaultdict, deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(node, parent):
    dp[node][0] = 0  # node가 우수 마을이 아닐 때
    dp[node][1] = residents[node]  # node가 우수 마을일 때

    for child in graph[node]:
        if child == parent:
            continue
        dfs(child, node)
        dp[node][0] += max(dp[child][0], dp[child][1])  # 자식이 우수 마을일 수도, 아닐 수도 있음
        dp[node][1] += dp[child][0]  # 자식은 우수 마을이 될 수 없음

n = int(input())  # 마을의 수
residents = [0] + list(map(int, input().split()))  # 각 마을의 주민 수 (1-based index)
graph = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, 0] for _ in range(n + 1)]  # dp[node][0]: node가 우수 마을이 아닐 때, dp[node][1]: node가 우수 마을일 때

dfs(1, -1)  # 1번 마을을 루트로 탐색 시작

print(max(dp[1][0], dp[1][1]))  # 루트에서 우수 마을 여부에 따라 최대값 출력