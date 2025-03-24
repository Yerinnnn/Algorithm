import sys
input = sys.stdin.readline

# DP 테이블 초기화
# dp[n][k][last_bit]: 길이가 n인 수열에서 인접한 비트 개수가 k이고 마지막 비트가 last_bit인 경우의 수
dp = [[[0, 0] for _ in range(101)] for _ in range(101)]

# 길이 1인 수열 초기화 (인접 비트 개수는 0)
dp[1][0][0] = 1  # 마지막 비트가 0
dp[1][0][1] = 1  # 마지막 비트가 1

# DP 테이블 채우기
for n in range(2, 101):
    for k in range(n):
        # 마지막 비트가 0인 경우: 이전 비트와 상관없이 인접 비트 개수는 변화 없음
        dp[n][k][0] = dp[n-1][k][0] + dp[n-1][k][1]
        
        # 마지막 비트가 1인 경우
        dp[n][k][1] = dp[n-1][k][0]  # 이전 비트가 0이면 인접 비트 개수 변화 없음
        if k > 0:
            dp[n][k][1] += dp[n-1][k-1][1]  # 이전 비트가 1이면 인접 비트 개수 1 증가

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    # 길이가 n이고 인접한 비트 개수가 k인 수열의 총 개수 (마지막 비트 0 + 마지막 비트 1)
    print(dp[n][k][0] + dp[n][k][1])