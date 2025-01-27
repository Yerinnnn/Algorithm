N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N)]

# 첫 번째 집의 비용 초기화
dp[0] = costs[0]

# 두 번째 집부터
for i in range(1, N):
    # 빨강으로 칠할 때: 이전 집의 초록/파랑 중 최소값 + 현재 빨강 비용
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    # 초록으로 칠할 때: 이전 집의 빨강/파랑 중 최소값 + 현재 초록 비용
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    # 파랑으로 칠할 때: 이전 집의 빨강/초록 중 최소값 + 현재 파랑 비용
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

print(min(dp[N-1]))  # 마지막 집까지의 최소 비용