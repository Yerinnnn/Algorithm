n, m = map(int, input().split())
men = sorted(map(int, input().split()))
women = sorted(map(int, input().split()))

# DP 테이블 초기화
dp = [[0] * (m + 1) for _ in range(n + 1)]

# DP 점화식 적용
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i-1][j-1] + abs(men[i-1] - women[j-1])
        
        # 남은 인원이 있는 경우 최소 불행도 업데이트
        if i > j:
            dp[i][j] = min(dp[i][j], dp[i-1][j])
        elif i < j:
            dp[i][j] = min(dp[i][j], dp[i][j-1])

print(dp[n][m])